class Atm(object): 
    def __init__(self,userName, depositAmt, withdrawalAmt, AccBalance): 
        self.userName = userName
        self.depostiAmt = depositAmt 
        self.AccBalance = AccBalance 
        self.withdrawalAmt = withdrawalAmt 
    def setbalance(self, depositAmt, withdrawalAmt, AccBalance): 
        self.AccBalance[depositAmt - withdrawalAmt] = AccBalance 
    def getbalance(self, AccBalance, depositAmt, withdrawalAmt): 
        return self.AccBalance[depositAmt - withdrawalAmt] 
    def getFinal(self): 
       return sum(self.depositAmt-self.withdrawalAmt) 
        
# Define some account holders 
user1 = Atm("User1", 12000, 3000) 
user2 = Atm("User2", 5000, 500) 

print(user1) 
print(user2)
