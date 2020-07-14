for i in range(6): #5줄을 출력할 수 있는 반복문
    for n in range(5,i-1,-1): #숫자앞의 공백을 출력하는 반복문
        print(end=" ")
    for j in range(1,i+1):
        print(j,end="")
    print()
