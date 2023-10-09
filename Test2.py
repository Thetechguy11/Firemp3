import machine
import utime

# Define GPIO pins for motor control
motor_pins = [machine.Pin(pin, machine.Pin.OUT) for pin in (17, 18, 19, 20)]

# Define the sequence of steps for the 28BYJ-48 motor
sequence = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]

# Set the initial direction and step delay (adjust as needed for speed)
clockwise = True
delay = 5  # Delay in milliseconds for moderate speed

def step_motor(clockwise):
    for _ in range(512):  # 512 steps is a full rotation for 28BYJ-48
        for i in range(4):
            for pin, state in zip(motor_pins, sequence[i]):
                pin.value(state)
            utime.sleep_ms(delay)

while True:
    if machine.Pin(1).value() == 1:
        clockwise = True
    elif machine.Pin(0).value() == 1:
        clockwise = False

    step_motor(clockwise=True)  # Rotate according to the current direction
