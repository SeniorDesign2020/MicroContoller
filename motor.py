#Import required libraries
import sys
import time
import RPi.GPIO as GPIO
import curses

class Controller:

    MotorBack1 = 36
    MotorBack2 = 38
    MotorBack = 40

    MotorFront1 = 37
    MotorFront2 = 35
    #MotorFront = 33
    
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        GPIO.setup(self.MotorFront1, GPIO.OUT)
        GPIO.setup(self.MotorFront2, GPIO.OUT)
        #GPIO.setup(self.MotorFront, GPIO.OUT)
        #GPIO.output(self.MotorFront, 0)

        GPIO.setup(self.MotorBack1, GPIO.OUT)
        GPIO.setup(self.MotorBack2, GPIO.OUT)
        GPIO.setup(self.MotorBack, GPIO.OUT)
        GPIO.output(self.MotorBack, 0)
        self.BackPWM = GPIO.PWM(self.MotorBack,100)
        self.BackPWM.start(0)
        self.BackPWM.ChangeDutyCycle(0)
        
        #self.direction = 0
    
    def front(self,f1,f2):
        GPIO.output(self.MotorFront1, f1)
        GPIO.output(self.MotorFront2, f2)
        #GPIO.output(self.MotorFront, f)

    def rear(self,b1,b2,b):
        GPIO.output(self.MotorBack1, b1)
        GPIO.output(self.MotorBack2, b2)
        self.BackPWM.ChangeDutyCycle(b)
    
    def steering(self):
        while True:
            char = screen.getch()
            if char == ord('d'):
                self.front(0, 1)
                self.rear(0,1,50)
            elif char == ord('a'):
                self.front(1, 0)
                self.rear(0,1,50)
            if char == ord('w'):
                self.rear(0, 1, 70)
                self.front(0,0)
            if char == ord('x'):
                break


if __name__ == '__main__':
    GPIO.cleanup()
    try:
        screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        screen.keypad(True)
        carCtrl = Controller()
        carCtrl.steering()
        GPIO.cleanup()
    except:
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin()
        carCtrl.BackPWM.stop()
        GPIO.cleanup()
        raise
