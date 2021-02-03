# Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction
#  if X is a multiple of 5, and Pooja's 
#  account balance has enough cash to perform the withdrawal 
#  transaction (including bank charges). For each successful 
#  withdrawal the bank charges 0.50 $US. Calculate Pooja's account
#   balance after an attempted transaction.

# def transaction(x,available_balnce):
    
#     if  x%5 == 0 and x<=available_balnce:
#         available_balnce = available_balnce-(x+0.50)
#         return available_balnce

#     return available_balnce

# print(transaction(182,120))  


class ATM(object):
    available_balance = 0

    def __init__(self,amount):
        self.amount = amount

    @classmethod   
    def credit_amount(cls,available_balance):
        cls.available_balance = available_balance

        print("Amount Credited",cls.available_balance) 

    @classmethod
    def debit_amount(cls,amount):
        if amount <= cls.available_balance and amount % 5 == 0:
            cls.available_balance = cls.available_balance - (amount+0.5)
            print("Available balance is",cls.available_balance)
            return 
        print("Error")
        return           

ATM.credit_amount(120)
ATM.debit_amount(130)