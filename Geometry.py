class RegularPolygon:
    def __init__(self, n, side,x,y):
        self.n= int(3)
        self.side= float(1)
        self.x= float(0)
        self.y= float(0)

    def set_n(self,n):
        self.n= int(n)

    def get_n(self):
        return self.n

    def set_side(self,side):
        self.side= float (side)

    def get_side(self):
        return self.side

    def set_x(self,x):
        self.x= float(x)

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = float (y)

    def get_y(self):
        return self.y

    def getPerimeter(self):
        return self.n * self.side

    def getArea(self):
        return (self.n/2) *self.x * self.y

