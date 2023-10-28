class Triangle():
   def __init__(self,l,b):
      self.l = l
      self.b = b 
      
   def set(self):
      if(self.l <= 0.0 or self.b <=0.0) or (self.l >= 20.0 or self.b >=20.0):
         print("enter breadth and length correctly")
   def get(self):
      print("the lenght is:",self.l)
      print("the breath is:",self.b)
   def perimeter(self):
       print("the perimeter is:",2*(self.l+self.b))
   def area(self):
      print("the area is:",self.l*self.b)
choice = 0
print("Ronit Satish Mehta 60009230207")
l = float(input("Enter length"))
b = float(input("Enter breadth"))
t = Triangle(l,b)
while choice != -1:
   choice = int(input("Enter choice"))
   match choice:
      case 1:
         t.set()
      case 2:
         t.get()
      case 3:
         t.perimeter()
      case 4:
         t.area()