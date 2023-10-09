import machine
import utime

# Define GPIO pins for motor control
motor_pins = [machine.Pin(pin, machine.Pin.OUT) for pin in (17, 18, 19, 20)]

# Define the sequence of steps for the 28BYJ-48 motor
# The sequence is for clockwise rotation; you can reverse it for counterclockwise
sequence = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]

# Set the initial direction and step delay (adjust as needed)
clockwise = True
delay = 5  # Delay in milliseconds

def step_motor(clockwise):
    for i in range(4):
        for pin, state in zip(motor_pins, sequence[i]):
            pin.value(state)
        utime.sleep_ms(delay)

while True:
    if machine.Pin(17).value() == 1:
        step_motor(clockwise=True)
    elif machine.Pin(16).value() == 1:
        step_motor(clockwise=False)
