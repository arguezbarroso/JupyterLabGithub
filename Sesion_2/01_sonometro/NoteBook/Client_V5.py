import time
import collections  # Ordered Dictionary.
import json
import logging

import requests # pylint: disable=E0401

# Handlers.
import GPS
import Rotary
import AZ8922
import InternalSensors
import NovaPM
import LCD_Handler
import Gases

# User Params.
endpoint = 'https://heimdalsoundcontrol.com/api/station'
SERIALNO = "HEIMDALSTA2"
LCD_TITLE = 'RUIDO DE FONDO V0.6'  # LCD Title. Max of 20 characters.
MEASURE_PERIOD = 300  # How often (seconds) we poll for measurements.
LCD_PERIOD = 10  # How often (seconds) the LCD switches between screens.
log_file = '/root/Angel/log.txt'

# Initialization.
logging.getLogger("urllib3").setLevel(logging.WARNING) # Disable DEBUG from the "requests" module.
logging.basicConfig(format='%(levelname)s:%(asctime)s %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S', filename=log_file, level=logging.DEBUG)
running = True  # Thread running condition.
packet_sent = False  # Packet has been sent succesfully.
LCD_start = False  # LCD has started to display information.

try:
    # LCD.
    LCD = LCD_Handler.LCD_Handler(title=LCD_TITLE, period=LCD_PERIOD)
    LCD.run_thread()

    # Rotary-Push.
    button = 23
    rotaryA = 9
    rotaryB = 24
    rotary = Rotary.Rotary(button, rotaryA, rotaryB)
    rotary.run_thread()

    # Sound level meter.
    port_AZ8922 = '/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_D-if00-port0'
    sound_level_meter = AZ8922.AZ8922(port_AZ8922)
    sound_level_meter.run_thread()

    # GPS.
    port_GPS = 16
    GPS = GPS.GPS(port_GPS)
    GPS.run_thread()

    # Particles sensor.
    port_NovaPM = '/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0'
    sensorP = NovaPM.NovaPM(port_NovaPM)
    sensorP.run_thread()

    # Gas sensor.
    port_gases = '/dev/serial/by-id/usb-Prolific_Technology_Inc._USB_2.0_To_COM_Device-if00-port0'
    gases = Gases.Gases(port_gases)
    gases.run_thread()

    # Internal sensors.
    port_tem = 18
    internal_sensors = InternalSensors.InternalSensors(port_tem)
    internal_sensors.run_thread()

    # Wait some extra time for the first measurement (initialize threads).
    time.sleep(5)

    # Main thread.
    while running:

        # Inintialize the JSON object.
        json_data = collections.OrderedDict()
        time.sleep(MEASURE_PERIOD)

        # Polling.
        sound_level = sound_level_meter.get_sonometry()
        pm25_mean, pm10_mean = sensorP.get_particles()
        NOX_mean, RED_mean = gases.get_gases()
        tem_mean, hum_mean, lum_mean, date = internal_sensors.get_measurements()
        position_GPS = GPS.get_position()

        # Backward compatibility with the 2260 sound level meter.
        sonometry = collections.OrderedDict()
        sonometry.update({'max': []})
        sonometry.update({'min': []})
        sonometry.update({'equivalent': []})
        sonometry.update({'eq_global': sound_level}) # Actual sonometry data.
        sonometry_json = json.dumps(sonometry)

        # Update the JSON object with the data gathered by the sensors.
        json_data.update({'sonometry': sonometry_json})
        json_data.update({'temperature': tem_mean})
        json_data.update({'humidity': hum_mean})
        json_data.update({'luminosity': lum_mean})
        json_data.update({'timestamp': time.time()})
        json_data.update({'GPS': position_GPS})
        json_data.update({'PM2_5': pm25_mean})
        json_data.update({'PM10': pm10_mean})
        json_data.update({'NOX': NOX_mean})
        json_data.update({'RED': RED_mean})
        json_data.update({'serialno': SERIALNO})
        
        packet_size = len(json.dumps(json_data))
        logging.info(f'Packet size:{packet_size} bytes')

        # Send the packet to the endpoint.
        try:
            requests.post(endpoint, timeout=15, json=json_data)
            logging.debug('Client: Packet sent.')
            packet_sent = True
        except requests.exceptions.RequestException as e:
            logging.exception('Network error')
            packet_sent = False

        # Send the data to the LCD.
        LCD.set_params(tem_mean, hum_mean, lum_mean, position_GPS, pm25_mean,
                       pm10_mean, sound_level, RED_mean, NOX_mean, packet_sent)

        # Notify the LCD that the first measurement has been completed.
        if not LCD_start:
            LCD.notify_thread()
            LCD_start = True
            logging.debug('First packet has been sent.')

# Stop the threads gracefully (close serial ports, clean LCD, etc).
finally:
    logging.debug('Executing finally clause.')
    running = False
    LCD.stop_thread()
    rotary.stop_thread()
    sound_level_meter.stop_thread()
    GPS.stop_thread()
    sensorP.stop_thread()
    gases.stop_thread()
    