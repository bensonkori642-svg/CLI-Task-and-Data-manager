
print("Welcome Best_Bank!!!!")
class Main():
    def __init__(self,name,age,gender,type_of_account):
        self.name= name
        self.age=age
        self.gender=gender
        self.type_of_account=type_of_account
    def users(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Account: {self.type_of_account}") 
class Bank(Main):
    def __init__(self,name,age,gender,type_of_account):
        super().__init__(name,age,gender,type_of_account)
        self.saving_account=0
        self.Normal_account=0
    def dep_saving(self):
        deposit=float(input("How much do you wish to deposit in your saving account?"))
        self.saving_account += deposit
        print("Deposit has been initiated successfully.....")
        print(f"A deposit of {deposit} has been confirmed!!\nThank you for being our customer\n")
    def dep_Normal(self):
        deposit=float(input("How much do you wish to deposit in your Normal account?"))
        self.Normal_account += deposit
        print("Deposit has been initiated successfully.....")
        print(f"A deposit of {deposit} has been confirmed!!\nThank you for being our customer\n")
    def withdraw_saving(self):
        withdraw=float(input("How much do you wish to withdraw:\n"))
        if withdraw >self.saving_account:
            print(f"Insufficient balance!!! Top up your account for higher withdraws!!")
        else:
            self.saving_account-=withdraw
            print("The withdrawal  has been initiated successfully.....")
            print(f"A withdrawal of {withdraw} has been confirmed!!\nThank you for being our customer\n")
        
    def withdraw_Normal(self):
        withdraw=float(input("How much do you wish to withdraw:\n"))
        if withdraw >self.Normal_account:
            print(f"Insufficient balance!!! Top up your account for higher withdraws!!")
        else:
            self.Normal_account-=withdraw
            print("The withdrawal  has been initiated successfully.....")
            print(f"A withdrawal of {withdraw} has been confirmed!!\nThank you for being our customer\n")


user_1=Bank("Ben",18,'male',type_of_account="saving")
user_1.users()
while True:
    acc=input("Which type of account do you want to deposit to...?\n 1.saving\n 2.Normal\n" )
    print(acc)
    if acc=="1":
        acc_type="saving"
    elif acc=="2":
        acc_type="Normal"
    else:
        print("Invalid input!!!\n Enter invalid input!!!\n")
        exit()

    print("=======MENU=======\n")
    print("1.Deposit\n 2.withdarw\n 3.check balance\n4.Exit\n")
    choice=(input("Choose an option above:\n"))
    if choice=='1':
        if acc=="1":
            user_1.dep_saving()
        else:
            user_1.dep_Normal()
    elif choice=="2":
        if acc=="1":
            user_1.withdraw_saving()
        else:
            user_1.withdraw_Normal()
    elif choice=="3":
        if acc=="1":
            print(f"Your saving account balance is: {user_1.saving_account}")
        else:
            print(f"Your Normal account balance is: {user_1.Normal_account}")
    elif choice=="4":
        print("Thank you for banking with us!!!\n")
        break
    else:    
        print("Invalid input!!!\n Enter invalid input and try again!!!\n")