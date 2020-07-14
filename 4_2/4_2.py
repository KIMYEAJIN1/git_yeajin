money=1
month=1
while money < 1000000:
    money=money*2
    month+=1
    if money >= 1000000:
        print(month,"달째 입니다!")
