from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5000)

import time
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed

# Create sensor and LED instances
light_sensor = GroveLightSensor(0)
led = GroveLed(5)

while True:  # Keep checking continuously
    light = light_sensor.light
    print('Light level:', light)
    
    if light < 300:
        led.on()  # Turn on LED if light is below threshold
    else:
        led.off()  # Turn off LED if light is above threshold
    
    time.sleep(2)  # Wait 2 seconds before checking again