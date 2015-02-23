#import GPIO libraries
import RPi.GPIO as GPIO
#import time
import time
#import random numbers
import random

#random number generator
x = random.randint(1,9)

#Sleep times
timeSleep1 = 0.5
timeSleep2 = 1

#Remove errors
GPIO.setwarnings(False)

#use raspberry pi bcm pin numbers
GPIO.setmode(GPIO.BOARD)

#sort LED pin numbers
WHITE_LED = 11

#setup GPIO outpu channels
GPIO.setup(WHITE_LED, GPIO.OUT)

#used for testing
#print x

#Start
print ("Count the number of flashes")

#Game loop
i = 0

while (i < x):
    time.sleep(timeSleep1)
    GPIO.output(WHITE_LED, True)
    time.sleep(timeSleep2)
    GPIO.output(WHITE_LED, False)
    time.sleep(timeSleep1)
    i += 1

#User input
answer = input("How many flashes did you see? ")

#Outputs
if (answer == x):
    print ("Correct, Well done!")

else:
    print ("Sorry wrong answer")

#Used for testing
#except KeyboardInterrupt:
#    GPIO.cleanup()

