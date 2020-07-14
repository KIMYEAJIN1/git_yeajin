sum=0
while(1):
    i = int(input("양수입력:")) #기본적으로 문자열로 입력받음
    if(i<=0):
       break
    sum+=i
print("누적된 값:",sum)
   
