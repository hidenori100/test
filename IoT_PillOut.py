from __future__ import print_function #파이썬3 문법사용 명시
import time #sleep 사용위해 명시
import RPI.GPIO as GPIO #GPIO라는 이름으로 모듈 사용


def measure():
	GPIO.output(GPIO_TRIGGER,True) #초음파 발생
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER,False) #초음파 발생 중지
	start=time() #시작시간 파악 
	stop=time() #종료시간 파악

	while GPIO.input(GPIO_ECHO)==0 : #들어온 값에 따라 시작시간 저장
		start=time()

	while GPIO.input(GPIO_ECHO)==1 : #들어온 값에 따라 종료시간 저장
		stop=time()
	
	elapsed = stop-start #거리계산 
	distance=(elapsed*34000)/2

	return distance


def measure_average() :
	distance1=measure()
	time.sleep(0.1)
	distance2=measure()
	time.sleep(0.1)
	distance3=measure()
	distance=distance1+distance2+distance3


	GPIO.setmode(GPIO.BCM)

	GPIO_TRIGGER = 23 #초음파 발생핀 
	GPIO_ECHO = 24 #초음파 수신핀
	GPIO_LED = 18 #LED 핀
	print ("Ultrasonic Measurement")

	GPIO.setup(GPIO_LED,GPIO.OUT) #18번 핀을 LED 출력으로
	GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
	GPIO.setup(GPIO_ECHO,GPIO.IN) 

	GPIO.output(GPIO_TRIGGER,False)

	try:
		while True:

			diastance=measure_average()
			time.sleep(1)

			if distance<=3:
				GPIO.output(GPIO_LED,GPIO.HIGH)
			else :
				GPIO.output(GPIO_LED,GPIO.LOW)

	except KeyboardInterrupt:
		GPIO.cleanup()





