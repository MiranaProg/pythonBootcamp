class Cylinder:
    pi= 3.14
    def __init__(self, height=1, radius=1):
        self.hgt = height
        self.rad = radius

    def volume(self):
        return (Cylinder.pi * self.rad **2 * self.hgt)


    def surface_area(self):

        return 2 *(Cylinder.pi * self.rad * self.hgt) + 2*(Cylinder.pi * self.rad **2)


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())