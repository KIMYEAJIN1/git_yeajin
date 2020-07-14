class MyClass:
    var= None
    def__init__(self):
        self.var= '안녕하세요!'
        print('MyClass인스턴스객체가생성되었습니다')
obj= MyClass() # ‘MyClass인스턴스객체가생성되었습니다’가출력됨
print(obj.var) # ‘안녕하세요’가출력됨
