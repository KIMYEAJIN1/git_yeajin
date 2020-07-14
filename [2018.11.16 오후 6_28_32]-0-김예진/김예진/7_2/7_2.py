import RPi.GPIO as GPIO #RPi.GPIO 모듈을 GPIO란 이름으로 사용
import time #time 함수 사용

LED=21 #LED를 GPIO 21에 연결
GPIO.setmode(GPIO.BCM) #핀 넘버링을 BCM 방식을 사용
GPIO_TRIGGER=26 # HC-SR04의 트리거 핀을 GPIO 26에 연결
GPIO_ECHO=19 # 에코핀을 GPIO 19에 연결
print ("Ultrasonic Distance Measurement") #Ultrasonic Distance Measurement 출력

GPIO.setup(GPIO_TRIGGER,GPIO.OUT) #초음파를 내보낼 트리거 핀 출력 모드로 설정
GPIO.setup(GPIO_ECHO,GPIO.IN) #반사파를 수신할 에코 핀 입력 모드로 설정
GPIO.setup(LED,GPIO.OUT) #동작이 감지되면 켜거나 꺼지게 하는 LED를 출력 모드로 설정

try: #블록 안의 구문을 수행하라
    while True: #While문의 조건이 TRUE이므로 안에 기술된 구문들이 무한하게 수행
        stop = 0 #stop 값을 0으로 설정
        start = 0 #start 값을 0으로 설정
        GPIO.output(GPIO_TRIGGER, False) #먼저 트리거 핀을 OFF 상태로 유지
        time.sleep(2) #2초간 코드를 실행하지 않고 멈춤
        GPIO.output(GPIO_TRIGGER, True) #10us 펄스 출력
        time.sleep(0.00001) #0.00001초간 코드를 실행하지 않고 멈춤
        GPIO.output(GPIO_TRIGGER, False) #트리거 핀을 OFF 상태로 설정

        while GPIO.input(GPIO_ECHO)==0:# 에코 핀이 ON되는 시점을 시작 시간으로 함
            start = time.clock() #start에 시작 시간을 측정하여 대입함
        while GPIO.input(GPIO_ECHO)==1:#에코 핀이 다시 OFF되는 시점을 반사파 수신 시간으로 함
            stop = time.clock() #stop에 수신 시간을 측정하여 대입함
            duration = stop-start #Calculate pulse length 
            if (stop and start): #stop 과 start 모두 TRUE일 경우 아래의 구문을 수행함
                distance = duration * 17000 # 음속은 편의상 340m/s로 계산_초음파는 반사파로  실제 이동 거리는 2배_ 떄문에  2로 나눔
                print("Distance : %.1f cm" %distance)#위에서 계산한 distance를 출력
                if distance >= 10:  #만약 distance가 10보다 크거나 같으면 다음의 구문을 실행함
                    GPIO.output(LED,True) #LED의 디지털 출력을 HIGH(1)로 설정 = LED가 켜짐
                else: #distance가 10보다 작으면 다음의 구문을 실행함
                    GPIO.output(LED,False) #LED의 디지털 출력을 LOW(0)로 설정 = LED가 꺼짐
except KeyboardInterrupt: #만약 KeyboardInterrupt 오류가 발생할경우 아래의 구문을 실행함
    print ("Ultrasonic Distance Measurement End") #Ultrasonic Distance Measurement End를 출력
    GPIO.cleanup() #GPIO를 초기화함
