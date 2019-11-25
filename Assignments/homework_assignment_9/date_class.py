# Guanyu Chen
# 0953074
# 11/24/2019
# MSITM 6341

class Date:
  def __init__(self, day, month,year):
    self.day = day
    self.month = month
    self.year = year
  def print_date(self):
    print(self.month + " " + str(self.day) + ", " + str(self.year))

  def change_date(self,day,month,year):
    self.day = day
    self.month = month
    self.year = year

d1 = Date(19,"June",2019)
d1.print_date()
d1.change_date(3,"August",2019)
d1.print_date()

d2 = Date(2,"May",2019)
d2.print_date()
d2.change_date(5,"September",2019)
d2.print_date()
