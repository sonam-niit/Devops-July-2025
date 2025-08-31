class Bank:
    def get_rate_of_intrest(self):
        return 6.5
    
class SBI(Bank):
    def display(self):
        print("Test SBI Method")
    
class ICICI(Bank):
    def get_rate_of_intrest(self): #method overriding
        return 8.7
    
sbi=SBI()
print("SBI Rate ofIntrest: ", sbi.get_rate_of_intrest()) #6.5
icici= ICICI()
print("ICICI Rate of intrest: ",icici.get_rate_of_intrest()) #8.7