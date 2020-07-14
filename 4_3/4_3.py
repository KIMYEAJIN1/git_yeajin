num=1
pum=0
while num>0:
    num=int(input("양수입력:"))
    if num <=0:
        print("누적된 값:",pum)
        break
    pum+=num
