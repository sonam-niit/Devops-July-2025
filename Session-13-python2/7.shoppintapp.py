class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        
    def login(self):
        print(f"{self.name} logged in with email: {self.email}")
        
class Customer(User):
    def __init__(self,name,email,address):
        super().__init__(name,email)
        self.address=address
    def place_order(self,item):
        print(f"{self.name} placed an order for {item} to be delivered at {self.address}")
        
class Seller(User):
    def __init__(self, name, email,store_name):
        super().__init__(name, email)
        self.store_name=store_name
        
    def add_product(self,product):
        print(f"{self.name} added {product} to their store {self.store_name}")
        
customer1=Customer("Alex","alex@microsoft.com","NewYork")
seller1= Seller("Bob","bob@outlook.com","Bob's Electronics")
#inherited functnality
customer1.login()
seller1.login()
#specific functionality
customer1.place_order("Laptop")
seller1.add_product("SmartPhone")


        