import RPi.GPIO as GPIO
import time

LedGpio1 = 4
LedGpio2 = 17
LedGpio3 = 18
LedGpio4 = 22
LedGpio5 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(LedGpio1, GPIO.OUT)
GPIO.setup(LedGpio2, GPIO.OUT)
GPIO.setup(LedGpio3, GPIO.OUT)
GPIO.setup(LedGpio4, GPIO.OUT)
GPIO.setup(LedGpio5, GPIO.OUT)


GPIO.output(LedGpio1, GPIO.HIGH)
time.sleep(0.5)
GPIO.output(LedGpio1, GPIO.LOW)
GPIO.output(LedGpio2, GPIO.HIGH)
time.sleep(0.5)
GPIO.output(LedGpio2, GPIO.LOW)
GPIO.output(LedGpio3, GPIO.HIGH)
time.sleep(0.5)
GPIO.output(LedGpio3, GPIO.LOW)
GPIO.output(LedGpio4, GPIO.HIGH)
time.sleep(0.5)
GPIO.output(LedGpio4, GPIO.LOW)
GPIO.output(LedGpio5, GPIO.HIGH)
time.sleep(0.5)
GPIO.output(LedGpio5, GPIO.LOW)


judge = 100
while judge == 100 :
    selectNum = int(input("選択してください（１：赤、２：青、３：緑、４：白、５：黄色、０：で終了）"))
    GPIO.output(LedGpio1, GPIO.LOW)
    GPIO.output(LedGpio2, GPIO.LOW)
    GPIO.output(LedGpio3, GPIO.LOW)
    GPIO.output(LedGpio4, GPIO.LOW)
    GPIO.output(LedGpio5, GPIO.LOW)
    if selectNum == 1:
        GPIO.output(LedGpio1, GPIO.HIGH)
    elif selectNum == 2:
        GPIO.output(LedGpio2, GPIO.HIGH)
    elif selectNum == 3:
        GPIO.output(LedGpio3, GPIO.HIGH)
    elif selectNum == 4:
        GPIO.output(LedGpio4, GPIO.HIGH)
    elif selectNum == 5:
        GPIO.output(LedGpio5, GPIO.HIGH)
    elif selectNum == 0 :
        break
GPIO.cleanup()
