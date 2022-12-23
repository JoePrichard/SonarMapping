# Import the necessary libraries
import time
import RPi.GPIO as GPIO

# Set up the GPIO pins for the sonar sensor
TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

# Set up an empty list to store the distance measurements
distances = []

# Set up a counter to keep track of the number of measurements taken
counter = 0

# Set the trigger to high for 2 microseconds to start the measurement
GPIO.output(TRIG, True)
time.sleep(0.00002)
GPIO.output(TRIG, False)

# Save the start time of the measurement
start = time.time()

# Wait for the echo pin to go high (indicating that the measurement is complete)
while GPIO.input(ECHO) == 0:
    start = time.time()

# Save the end time of the measurement
stop = time.time()

# Calculate the distance based on the time elapsed
distance = (stop - start) * 34300 / 2

# Add the distance to the list of measurements
distances.append(distance)

# Increment the counter
counter += 1

# Print the distance
print("Distance:", distance, "cm")

# Repeat the measurement process for a total of 360 measurements (one measurement every degree)
while counter < 360:
    # Set the trigger to high for 2 microseconds to start the measurement
    GPIO.output(TRIG, True)
    time.sleep(0.00002)
    GPIO.output(TRIG, False)

    # Save the start time of the measurement
    start = time.time()

    # Wait for the echo pin to go high (indicating that the measurement is complete)
    while GPIO.input(ECHO) == 0:
        start = time.time()

    # Save the end time of the measurement
    stop = time.time()

    # Calculate the distance based on the time elapsed
    distance = (stop - start) * 34300 / 2

    # Add the distance to the list of measurements
    distances.append(distance)

    # Increment the counter
    counter += 1

    # Print the distance
    print("Distance:", distance, "cm")

# Clean up the GPIO pins
GPIO.cleanup()

# Print the list of distances
print(distances)
