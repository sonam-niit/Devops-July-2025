class Student:
    def __init__(self,id,name,marks):
        self.name= name
        self.id=id
        self.marks=marks
    def display(self):
        print(f"Name: {self.name} Id: {self.id}")
    def is_passed(self):
        result=self.marks>=40
        if result:
            print("Passed")
        else:
            print("Failed")
        
        
stu1=Student("100","Sonam Soni",96) #object of student class
stu1.display()
stu1.is_passed()