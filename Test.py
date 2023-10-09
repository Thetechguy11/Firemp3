import machine
import utime

# Define GPIO pins for motor control
step_pin = machine.Pin(17, machine.Pin.OUT)
dir_pin = machine.Pin(16, machine.Pin.OUT)

# Set the initial direction and step delay (adjust as needed)
clockwise = True
delay = 2  # Delay in milliseconds

def step_motor(clockwise):
    if clockwise:
        dir_pin.value(1)  # Set direction pin for clockwise rotation
    else:
        dir_pin.value(0)  # Set direction pin for counterclockwise rotation

    # Generate steps to make the motor move
    for _ in range(200):  # 200 steps is a full rotation for most motors
        step_pin.value(1)
        utime.sleep_ms(delay)
        step_pin.value(0)
        utime.sleep_ms(delay)

while True:
    if machine.Pin(17).value() == 1:
        step_motor(clockwise=True)
    elif machine.Pin(16).value() == 1:
        step_motor(clockwise=False)
