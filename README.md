# Firemp3
import machine
import neopixel
import time

# Define the number of NeoPixels and their pin
num_pixels = 1
pin = machine.Pin(0)  # You can adjust the pin number as needed

# Create a NeoPixel object
pixels = neopixel.NeoPixel(pin, num_pixels)

while True:
    # Change the color to yellow
    pixels[0] = (255, 255, 0)  # RGB values for yellow
    pixels.write()
    time.sleep(1)  # Wait for 1 second

    # Change the color to orange
    pixels[0] = (255, 165, 0)  # RGB values for orange
    pixels.write()
    time.sleep(1)  # Wait for 1 second
