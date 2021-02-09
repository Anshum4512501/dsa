# def saving(cls):
#     cls.account_type = "Saving Account"
#     return cls

# def checking(cls):
#     cls.account_type = "Checking Account"
#     return cls
# @saving
# class BankSavingAccountone:
#     pass
# @saving
# class BankSavingAccounttwo:
#     pass
# @checking
# class BankChecingAccountone:
#     pass

# @checking
# class BankChecingAccounttwo:
#     pass

# print(BankSavingAccountone.__dict__)

# USE PARAMETERIZED DECORATOR RATHER BASRE ONE

def account_type(type_):
    def decorator(cls):
        cls.account_type = type_
        return cls

    return decorator
@account_type("Saving Account")
class BankSavingAccountone:
    pass
# @saving
# class BankSavingAccounttwo:
#     pass
# @checking
# class BankChecingAccountone:
#     pass

# @checking
# class BankChecingAccounttwo:
#     pass

print(BankSavingAccountone.__dict__)

