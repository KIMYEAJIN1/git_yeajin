import RPi.GPIO as GPIO #RPi.GPIO 모듈을 GPIO란 이름으로 사용
import time #time 함수 사용

LED=21 #LED를 GPIO 21에 연결
PIN=20 # GPIO 20번에  연결
GPIO.setmode(GPIO.BCM) #핀 넘버링을 BCM 방식을 사용
GPIO.setup(PIN,GPIO.IN) #적외선을 감지할 PIN을 입력 모드로 설정
GPIO.setup(LED,GPIO.OUT) #동작이 감지되면 켜거나 꺼지게 하는 LED를 출력 모드로 설정

while True: #While문의 조건이 TRUE이므로 안에 기술된 구문들이 무한하게 수행
    GPIO.output(LED,0) #LED의 디지털 출력을 LOW(0)로 설정 = LED가 꺼짐
    if GPIO.input(PIN) == true: #PIN의 디지털 값을 읽어 그 값이 TRUE(모션이 감지됨) 일때 다음의 구문을 실행함
        GPIO.output(LED,1) #LED의 디지털 출력을 HIGH(1)로 설정 = LED가 켜짐
        time.sleep(1) #1초간 코드를 실행하지 않고 멈춤
