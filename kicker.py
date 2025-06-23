import RPi.GPIO as GPIO
from time import sleep

# The pins we will use to drive the motor on the Raspberry Pi
MOTOR_PIN_ARRAY = [23,22,27,17]

HARD_KICK_BUTTON_PIN = 0
SOFT_KICK_BUTTON_PIN = 0

# Delay between steps in seconds
##########################################
# STEP DELAY VALUES: Copy and paste below.
# DELAY = (60/RPM) / 4096
# 1/2 RPM: 0.029297
#   1 RPM: 0.014648
#   2 RPM: 0.007324
#   5 RPM: 0.002930
#  10 RPM: 0.001465
#  15 RPM: 0.000977
#  20 RPM: 0.000732
##########################################
# Paste value here:

step_delay = 0.014648


# Define the stepper motor sequence
step_sequence = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

steps_per_hard_kick = 1000
steps_per_soft_kick = 500

def set_up_pins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for pin in MOTOR_PIN_ARRAY:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        print(f"Pin {pin} set as output")

    GPIO.setup(HARD_KICK_BUTTON_PIN, GPIO.IN)
    GPIO.setup(SOFT_KICK_BUTTON_PIN, GPIO.IN)

    

def step(direction, steps):
    global motor_step_counter

    print(f"step: {direction} {steps}")
    for i in range(steps):
        for pin in range(len(MOTOR_PIN_ARRAY)):
            GPIO.output(MOTOR_PIN_ARRAY[pin], step_sequence[motor_step_counter][pin])
        if direction == True:
            motor_step_counter = (motor_step_counter + 1) % 8
        elif direction == False:
            motor_step_counter = (motor_step_counter - 1) % 8
        else:
            print("That didn't work")
        sleep(step_delay)

def kick(number_of_steps):
    print("hard kick")
    step(True, number_of_steps)
    step(False, number_of_steps)
    


if __name__ == "__main__":

    while True:
        #If the button is depressed, kick the ball
        kick(steps_per_hard_kick)