print("Welcome to Task Manager!")
process=True
class manager():
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def user_details(self):
        print(f"Name : {self.username}")
        print(f"Password : {self.password}")
class task(manager):
    users={}
    @classmethod 
    def login_page(cls):
        username=input("Please enter your name!\n")
        password=input("Please enter your password!\n")
        user=cls.users.get(username)
        if user and user.password==password:
            print("login is successful!!")
        else:
            print("Incorrect details!!! Try Again!!")
    @classmethod
    def signup_page(cls):
        username=input("Please enter your name!\n")
        if username in cls.users:
            print("Username already exists!!")
            return
        password=input("Please enter your password!\n")
        cls.users[username]=manager(username, password)
        print("login successfully!!") 
while  process:
    print("Enter '1' to login / '2' to signup / '3' to exit")
    choice=input("Please enter a number to proceed..\n")
    print(choice)
    if choice=='1':
        task.login_page()
    elif choice=='2':
        task.signup_page()
    elif choice=='3':
        print("You have exited!!!")
        process=False
    else:
        print("Invalid input!!! Try Again!!")



    