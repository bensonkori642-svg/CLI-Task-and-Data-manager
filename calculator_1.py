# def display():
#     print("hi")
#     display()
# display()
# def add (a,b):
#     return (a+b)
# def multiply(a,b):    
#     return (a*b)
# def Division(a,b):
#     return (a/b)
# def subtract(a,b):
#     return (a-b)

# operators_dict={
#     "+":add,
#     "-":subtract,
#     "*":multiply,
#     "/":Division
# }
# def recoz():
#     number_1=(input("please enter your 1st number..."))
#     for key in operators_dict:
#         print(key)
#     loop=True
#     while loop:
#         key_pick=input('please pick one operation...')
#         number_2=("please enter you 2nd number...")
#         calc_fuction=operators_dict[key_pick]
#         ouput=calc_fuction(number_1,number_2)
#         print=ouput
#         print(f"{number_1} {key_pick} {number_2} = {ouput}")
#         action_keys=(f"press C to continue / x to exit / S to start a new calculation").lower()
#         print(action_keys)
#         if action_keys == C:
#             number_1 = output
#         elif action_keys ==X:
#             loop=False
#             recoz()
#         else:
#             loop=False
#             print("That's all folks")
# recoz()
            

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def division(a, b):
    return a / b

def subtract(a, b):
    return a - b


operators_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}


def recoz():
    number_1 = float(input("Please enter your 1st number: "))

    for key in operators_dict:
        print(key)

    loop = True

    while loop:
        key_pick = input("Please pick an operation: ")

        number_2 = float(input("Please enter your 2nd number: "))

        calc_function = operators_dict[key_pick]
        output = calc_function(number_1, number_2)

        print(f"{number_1} {key_pick} {number_2} = {output}")

        action = input(
            "Press C to continue / X to exit / S to start new: "
        ).lower()

        if action == "c":
            number_1 = output
        elif action == "s":
            recoz()
            return   # stops current function
        else:
            loop = False
            print("That's all folks!")


recoz()

