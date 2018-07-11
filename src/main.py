import time
import motor, sensor

print("Starting...")

try:
    while True:
        sensors = []
        sensorOutput = ""

        for i in range(0, len(sensor.echoPins)): sensors.append(sensor.value(i))
        
        for i in range(0, len(sensors)):
            sensorOutput += " Sensor " + str(i) + ": " + str(sensors[0] * 100).ljust(3) + "cm"
        
        print("Output:" + sensorOutput)

        for i in range(0, len(sensors)):
            motor.value(i, sensors[i])

        time.sleep(0.2)
        
except KeyboardInterrupt:
    print("Stopped.")