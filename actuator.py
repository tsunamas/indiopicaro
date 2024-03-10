import RPi.GPIO as GPIO
from time import sleep

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

class Actuator:
    def __init__(self,Ena,In1,In2):
        GPIO.setmode(GPIO.BCM)
        self.Ena = Ena
        self.In1 = In1
        self.In2 = In2
        GPIO.setup(self.Ena,GPIO.OUT)
        GPIO.setup(self.In1,GPIO.OUT)
        GPIO.setup(self.In2,GPIO.OUT)
        self.pwm = GPIO.PWM(self.Ena, 1000)
        self.pwm.start(0)
        self.pwm.ChangeDutyCycle(100)
        
    def extend(self):
        print('Extending')
        GPIO.output(self.In1, GPIO.HIGH)
        GPIO.output(self.In2, GPIO.LOW)
        
    def retract(self):
        print('Retracting')
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.HIGH)
        
    def cleanup(self):
        print("Exit - Cleanup")
        GPIO.cleanup() # this ensures a clean exit 
                
        
#actuator = Actuator(25,24,23)


#try: 
#   while True:
#        actuator.extend()
#        sleep(6)
#       actuator.retract()
#       sleep(6)
#except:
#        print("Exit.")
#        GPIO.cleanup() # this ensures a clean exit 
        
