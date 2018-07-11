import gpiozero

echoPins = [14, 27, 11, 12, 20]
trigPins = [ 3, 23, 10,  5, 26]
sensors = []

if len(echoPins) != len(trigPins): raise ValueError("Length of trigPins does not match length of echoPins")

for i in range(0, len(echoPins)):
    sensors.append(gpiozero.DistanceSensor(echoPins[i], trigPins[i], max_distance = 1))
    print(sensors[i].distance)

def value(id):
    try:
        return sensors[id].distance
    except:
        print("Error on sensor " + str(id))
        return 1