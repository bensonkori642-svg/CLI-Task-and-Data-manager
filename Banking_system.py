# #Banking system using oop...
# class User():
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def user_details(self):
#         print("....personal details....\n")
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Gender: {self.gender}")
# class Bank(User):
#     def __init__(self,name,age,gender):
#         super().__init__(name,age,gender)
#         def Bal(self,amount):
#             self.amount=amount
#             self.amount=0
#             print(f"Your balance is {self.amount}")
#         def Deposit(self,deposit):
#             self.deposit=deposit
#             balance=self.deposit + self.amount
#             print(f"Your account balance is : {balance}")
#         def Withdraw(self,withdraw):
#             self.withdraw=withdraw
#             if withdraw > balance:
#                 print("Insufficient balance in your account!!!Top_up your account to higher withdraws!!!")
#             else:
#                 print("Your withdrawal of {self.withdraw} is successful! Thankyou!")
#             updated_balance=balance -self.withdraw
#             print("Your balance is {balance} after a successful withdrawal of {self.withdraw}")
# User("|Ben",16,"male")
# Bank("|Ben",16,"male")


# Banking system using OOP

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def user_details(self):
        print("....Personal Details....\n")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0   # initialize balance properly

    def show_balance(self):
        print(f"Your balance is {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully!")
        print(f"Your account balance is: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance in your account!")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful!")
            print(f"Your updated balance is: {self.balance}")


# ---- Testing the system ----
user1 = Bank("Benson", 22, "Male")

user1.user_details()
user1.show_balance()

user1.deposit(1000)
user1.withdraw(500)
user1.withdraw(700)


