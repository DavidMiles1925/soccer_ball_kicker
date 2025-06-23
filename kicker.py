import RPi.GPIO as GPIO
from time import sleep

# The pins we will use to drive the motor on the Raspberry Pi
MOTOR_PIN_ARRAY = [23,22,27,17]

# Pins used for button input
HARD_KICK_BUTTON_PIN = 24
SOFT_KICK_BUTTON_PIN = 25

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
#  20 RPM: 0.000733
#  40 RPM: 0.000366
##########################################
# Paste value here:

step_delay = 0.000732


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

# This variale is used by the step() function for mathematically determining which item in the step_sequence array to call.
motor_step_counter = 0

# These variables determine how far to move the motor for each type of kick.
steps_per_hard_kick = 1000
steps_per_soft_kick = 500

# This function prepares the GPIO pins on the Raspberry Pi for use.
def set_up_pins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for pin in MOTOR_PIN_ARRAY:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        print(f"Pin {pin} set as output")

    GPIO.setup(HARD_KICK_BUTTON_PIN, GPIO.IN)
    GPIO.setup(SOFT_KICK_BUTTON_PIN, GPIO.IN)

    
# This function moves the motor.
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


# This function is used to "kick the ball"
def kick(number_of_steps):
    print("hard kick")
    step(True, number_of_steps)
    sleep(0.1)
    step(False, number_of_steps)
    sleep(2)
    


if __name__ == "__main__":
    set_up_pins()

    while True:
        if GPIO.input(HARD_KICK_BUTTON_PIN) == True:
            print("push")
            sleep(1)
            kick(steps_per_hard_kick)

        if GPIO.input(SOFT_KICK_BUTTON_PIN) == False:
            print("push2")
            #kick(steps_per_soft_kick)