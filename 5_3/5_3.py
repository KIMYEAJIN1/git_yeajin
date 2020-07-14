class Shape:
    name=None
    area=0
    def __init__(self,name,area):
        self.name=name
        self.area=area
        
    def showMe(self) :
        print("도형이름",self.name," 도형 면적",self.area)

triangle = Shape("삼각형",3)
circle = Shape("원형",4)
triangle.showMe()
circle.showMe()
