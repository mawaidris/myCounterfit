from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5000)

import time
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
    #The import time statement imports the Python time module that will be used later in this assignment.
    #The from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor statement imports the GroveLightSensor from the CounterFit Grove shim Python libraries. This library has code to interact with a light sensor created in the CounterFit app.

light_sensor = GroveLightSensor(0)
    #The line light_sensor = GroveLightSensor(0) creates an instance of the GroveLightSensor class connecting to pin 0 - the CounterFit Grove pin that the light sensor is connected to.

if True:
    light = light_sensor.light
    print('Light level:', light)
    #This will read the current light level using the light property of the GroveLightSensor class. This property reads the analog value from the pin. This value is then printed to the console. i exchanged while to if btw cuz i hate watching an infinite shi.

time.sleep(1)
    ##The time.sleep(1) statement pauses the program for 1 second before the next reading. This is done to reduce the power consumption of the light sensor and to avoid flooding the console with too many readings in a short period of time.


