# Guanyu Chen
# 0953074
# 12/08/2019
# MSITM 6341

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def print_dimensions(self):
    print("width x height: " + str(self.width) + " x " +str(self.height))

  def get_area(self):
    area = (self.height) * (self.width)
    return area

  def get_perimeter(self):
    perimeter = ((self.height) + (self.width)) * 2
    return perimeter

r1 = Rectangle (5, 10)
r1.print_dimensions()
print("area is: " + str(r1.get_area()))
print("perimeter is: " + str(r1.get_perimeter()))