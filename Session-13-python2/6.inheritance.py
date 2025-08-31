class Parent:
    def __init__(self,name):
        self.name=name #parent class variable
    def testParent(self):
        print(f"Hello From Parent {self.name}")

class Child(Parent): #inheritance implemented
    def __init__(self, name,test):
        super().__init__(name) # pass name from child to parent
        self.test=test #child class variable
    def testChild(self):
        print(f"Hello From Child {self.test}")
        
child1=Child("Sonam Soni","hello")  #pass value to parent class constructor
child1.testParent()#child can call parent class method
child1.testChild()