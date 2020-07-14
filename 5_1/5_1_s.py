n1=int(float(input("첫번째 정수를 입력하세요 : "))) #소수점 버림_정수가 아닌 실수 입력시 오류 제한
n2=int(input("두번째 정수를 입력하세요 : "))
answer = None #파이썬은 변수를 대입해야 계산을 진행할 수 있음_answer 정의 안해도 됨

def sum(): #함수정의 들어쓰기 유의할 것
    global answer
    answer=n1+n2; #global 정의 전에는 지역변수
    print("두수의 덧셈결과 :",answer)

def minus():
    global answer
    answer=n1-n2; #만얃 여기서 global answer을 +=1 한다면 결과값은 저장된 answer값에 계산
    print("두수의 뺄셈결과 :",answer)

def product():
    global answer
    answer=n1*n2;
    print("두수의 곱셈결과 :",answer)

def devide():
    global answer
    answer=n1/n2;
    print("두수의 나눗셈 결과 :",answer)

sum()
minus()
product()
devide()
