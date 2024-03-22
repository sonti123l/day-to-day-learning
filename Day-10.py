import calculator_art
from replit import clear

# prints the calculator logo
print(calculator_art.logo)
# starting process of claculator
user_num = float(input("What's the first number?: "))
operation_list = ["+", "-", "*", "%"]
for oper in operation_list:
    print(f"{oper}")


# user picks o    
def operators():
    user_option = input("Pick an operation: ")
    return user_option


# calculator

def calculator(operation, number):
    if operation == "+":
        second_num = float(input("What's the next number? "))
        addition = number + second_num
        print(f"{number} + {second_num} = {addition}")
        user_choice = input(
            f"Type 'y' to continue calculating with {addition},or type 'n' to start a new calculation: ")
        return addition, user_choice
    elif operation == "-":
        second_num = float(input("What's the next number? "))
        subtraction = number - second_num
        print(f"{number} - {second_num} = {subtraction}")
        user_choice = input(
            f"Type 'y' to continue calculating with {subtraction},or type 'n' to start a new calculation: ")
        return subtraction, user_choice
    elif operation == "*":
        second_num = float(input("What's the next number? "))
        multiplication = number * second_num
        user_choice = input(
            f"Type 'y' to continue calculating with {multiplication},or type 'n' to start a new calculation: ")
        return multiplication, user_choice
    elif operation == "%":
        second_num = float(input("What's the next number? "))
        division = number % second_num
        user_choice = input(
            f"Type 'y' to continue calculating with {division},or type 'n' to start a new calculation: ")
        return division, user_choice
    else:
        return "provide the correct inputs"


# last res new calculation 
def on_continuation(last_res):
    next_calculation = operators()
    calculator(operation=next_calculation, number=last_res)


# first calculation
# second calculation
result, choice = calculator(operation=operators(), number=user_num)
if choice == 'y':
    on_continuation(last_res=result)
elif choice == 'n':
    clear()
    user_num_2 = int(input("What's the first number? "))
    for oper in operation_list:
        print(f"{oper}")
    calculator(operation=operators(), number=user_num_2)
else:
    print("no calculations done here.")
