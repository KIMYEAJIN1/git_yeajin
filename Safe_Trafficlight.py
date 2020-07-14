import RPi.GPIO as GPIO #RPi.GPIO 모듈을 GPIO란 이름으로 사용
import time #time 함수 사용

BLED=16 #BLED를 GPIO 16에 연결
RLED=21 #RLED를 GPIO 21에 연결
BUTTON=19 #스위치를 GPIO 19에 연결
MOTOR=17 #MOTOR를 GPIO 17에 연결
PIR=5 #모션센서를 GPIO 5에 연결
GPIO.setmode(GPIO.BCM) #핀 넘버링을 BCM 방식을 사용
GPIO.setup(BLED,GPIO.OUT) #BLED를 출력 모드로 설정
GPIO.setup(RLED,GPIO.OUT) #RLED를 출력 모드로 설정
GPIO.setup(BUTTON,GPIO.IN,GPIO.PUD_UP) #스위치를 입력 모드로 설정하며 PULLUP으로 연결함
GPIO.setup(MOTOR,GPIO.OUT) #MOTOR를 출력 모드로 설정
GPIO.setup(PIR,GPIO.IN) #적외선을 감지할 PIR을 입력 모드로 설정
p=GPIO.PWM(MOTOR,50) #p를 전역변수로 지정하고 MOTOR의 출력 싸이클을 50%로 함
left_angle=12.5 #left_angle를 전역변수로 지정하고 그 값을 12.5으로 함
right_angle=12.5 #right_angle를 전역변수로 지정하고 그 값을 12.5으로 함
i=0 #i를 전역변수로 지정하고 그 값을 0으로 함

def doAngle(angle): #doAngle라는 함수를 선언하며 함수는 angle을 인자로 가지며, 함수의 기능은 아래 기술된 구문과 같음
    p.changeDutyCycle(angle) #MOTOR를 angle인자 값에 따라 회전시킴
    time.sleep(0.5) #0.5초간 코드를 실행하지 않고 멈춤

def loop(): #loop라는 함수를 선언하며 함수의 기능은 아래 기술된 구문과 같음
    GPIO.output(BLED,False) #BLED의 디지털 출력을 LOW(0)로 설정 = LED가 꺼짐
    time.sleep(0.5) #0.5초간 코드를 실행하지 않고 멈춤
    GPIO.output(BLED,True) #BLED의 디지털 출력을 HIGH(1)로 설정 = LED가 켜짐
    global i #전역변수 i를 사용함
    i+=1 #전역변수 i의 값을 +=1로 지정함

try: #블록 안의 구문을 수행하라
    GPIO.output(RLED,True) #RLED의 디지털 출력을 HIGH(1)로 설정 = LED가 켜짐
    GPIO.output(BLED,False) #BLED의 디지털 출력을 LOW(0)로 설정 = LED가 꺼짐
    while True: #While문의 조건이 TRUE이므로 안에 기술된 구문들이 무한하게 수행
        if GPIO.input(PIR)==True: #PIR의 디지털 값을 읽어 그 값이 TRUE(모션이 감지됨) 일때 다음의 구문을 실행함
            print("Waiting") #화면에 Waiting을 출력함
        if not GPIO.input(BUTTON): #BUTTON의 디지털 값을 읽어 그 값이 TRUE(버튼이 입력)일때 다음의 구문을 실행함
            print("Button") #화면에 BUTTON을 출력함
            time.sleep(0.5) #0.5초간 코드를 실행하지 않고 멈춤
            p.start(7.5)#MOTOR의 PWM핀의 출력을 7.5로 설정해 수행함
            GPIO.output(RLED,False) #RLED의 디지털 출력을 LOW(0)로 설정 = LED가 꺼짐
            GPIO.output(BLED,True) #BLED의 디지털 출력을 HIGH(1)로 설정 = LED가 켜짐
            doAngle(left_angle) #doAngle라는 함수를 호출하며 인자의 값을 left_angle로 지정해 실행함
            p.stop() #MOTOR의 작동을 멈춤
            time.sleep(3) #3초간 코드를 실행하지 않고 멈춤
            while i<5: # i의 값이 5미만일 경우 다음 구문을 수행함
                loop() #loop 함수를 호출
            global i #전역변수 i를 사용함
            i=0 #전역변수 i의 값을 0으로 지정함
            p.start(7.5) #MOTOR의 PWM핀의 출력을 7.5로 설정해 수행함
            doAngle(right_angle) #doAngle라는 함수를 호출하며 인자의 값을 right_angle로 지정해 실행함
            GPIO.output(RLED,True) #RLED의 디지털 출력을 HIGH(1)로 설정 = LED가 켜짐
            GPIO.output(BLED,False) #BLED의 디지털 출력을 LOW(0)로 설정 = LED가 꺼짐
            p.stop() #MOTOR의 디지털 출력을 LOW(0)로 설정 = MOTOR의 작동을 멈춤
        else:
            doAngle(right_angle) #doAngle라는 함수를 호출하며 인자의 값을 right_angle로 지정해 실행함
            p.stop() #MOTOR의 작동을 멈춤
            
except KeyboardInterrupt:  #만약 KeyboardInterrupt 오류가 발생할경우 아래의 구문을 실행함
    p.stop() #MOTOR의 디지털 출력을 LOW(0)로 설정 = MOTOR의 작동을 멈춤
    GPIO.output(RLED,False) #RLED의 디지털 출력을 LOW(0)로 설정 = LED가 꺼짐
    GPIO.output(BLED,False) #BLED의 디지털 출력을 LOW(0)로 설정 = LED가 꺼짐
    GPIO.cleanup() #GPIO를 초기화함

