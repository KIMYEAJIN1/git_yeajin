class Shape:
    name=None
    area=0
    def __init__(self,name,area):
        self.name=name
        self.area=area
        
    def showMe(self) :
        print("도형이름",self.name," 도형 면적",self.area)

class Circle(Shape):
    rad=0
    def __init__(self,name,rad):
        self.name=name
        self.rad=rad
        
    def computeArea(self):
        global area
        area = 3.14*self.rad**2

    def showMe(self) :
        print("도형이름",self.name,"반지름",self.rad," 도형 면적",area)

    
obj=Circle("원형",4)
obj.computeArea()
obj.showMe()

