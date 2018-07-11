import gpiozero

motorPins = [15, 24, 18, 16, 25]
motors = []

for i in range(0, len(motorPins)): motors.append(gpiozero.PWMLED(motorPins[i], initial_value = 0))

def value(id, amount):
    # The value is negated due to the fact that the vibrators get lighter as the distance sensors lose proximity.
    motors[id].value = 1 - amount