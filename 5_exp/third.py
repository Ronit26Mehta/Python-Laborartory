student_details={"name":[],"id":[],"maths":[],"chemistry":[],"physics":[],"total":[]}
class descending():
    def __init__(self,studen_details):
        self.student_details=student_details;
        self.sum1=0
    def calc(self):
       for i in range(len(student_details["name"])):
           self.sum1 = self.student_details["chemistry"][i]+self.student_details["maths"][i]+self.student_details["physics"][i]
           self.student_details["total"].append(self.sum1)
    def display(self):
        for i in range(len(self.student_details["total"])-1):
            for j in range(len(self.student_details["total"])-i-1):
                if self.student_details["total"][j] < self.student_details["total"][j+1]:
                    temp1=self.student_details["name"][j+1]
                    temp2=self.student_details["id"][j+1]
                    temp3=self.student_details["maths"][j+1]
                    temp4=self.student_details["physics"][j+1]
                    temp5=self.student_details["chemistry"][j+1]
                    temp6=self.student_details["total"][j+1]
                    self.student_details["name"][j+1]= self.student_details["name"][j]
                    self.student_details["name"][j]=temp1
                    self.student_details["id"][j+1]=self.student_details["id"][j]
                    self.student_details["id"][j]=temp2
                    self.student_details["maths"][j+1]=self.student_details["maths"][j]
                    self.student_details["maths"][j]=temp3
                    self.student_details["chemistry"][j+1]=self.student_details["chemistry"][j]
                    self.student_details["chemistry"][j]=temp5
                    self.student_details["physics"][j+1]=self.student_details["physics"][j]
                    self.student_details["physics"][j]=temp4
                    self.student_details["total"][j+1]=self.student_details["total"][j]
                    self.student_details["total"][j]=temp6
        for i in range(len(self.student_details["name"])):
            print(i,self.student_details["name"][i],self.student_details["total"][i])
number = int(input("Enter the number of students data to be entered"))
for i in range(number):
    name = str(input("Enter name:"))
    id1   = str(input("Enter id:"))
    maths_marks = int(input("Enter marks for maths:"))
    chemistry_marks = int(input("Enter marks for chemistry:"))
    physics_marks = int(input("Enter marks for physics"))
    student_details["name"].append(name)
    student_details["id"].append(id)
    student_details["maths"].append(maths_marks)
    student_details["chemistry"].append(chemistry_marks)
    student_details["physics"].append(physics_marks)
dec = descending(student_details)
dec.calc()
dec.display()

