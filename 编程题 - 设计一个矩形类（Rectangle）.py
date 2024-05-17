class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def square(self):
        square=self.width*self.length
        return square
    def perimeter(self):
        perimeter=2*(self.length+self.width)
        return perimeter
    def scale(self,factor):
        return factor*factor*self.square(),factor*self.perimeter()
l,w,f=map(float,input().split())
rect_1=Rectangle(l,w)
print(f'area:{rect_1.square()}')
print(f'perimeter:{rect_1.perimeter()}')
after=rect_1.scale(f)
print(f'after scale,area:{after[0]}')
print(f'after scale,perimeter:{after[1]}')