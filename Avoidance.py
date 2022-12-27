import time
import RPi.GPIO as GPIO

# Set up the hypersonic sensor
GPIO.setmode(GPIO.BOARD)
TRIG = 7
ECHO = 11

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

# Set the trigger to False (low)
GPIO.output(TRIG, False)

# Allow the sensor to settle
time.sleep(0.5)

# Main loop
while True:
  # Send a pulse
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  # Record the start and end times of the pulse
  while GPIO.input(ECHO)==0:
    pulse_start = time.time()
  while GPIO.input(ECHO)==1:
    pulse_end = time.time()

  # Calculate the distance to the nearest obstacle
  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150
  distance = round(distance, 2)

  # Take action based on the distance to the nearest obstacle
  if distance < 20:
    print("Too close! Stopping.")
    PWM.setMotorModel(0,0,0,0)
    break
  else:
    print("Distance:", distance, "cm")
    PWM.setMotorModel(2000,2000,2000,2000) 
    time.sleep(0.5)

# Clean up the GPIO pins
GPIO.cleanup()
