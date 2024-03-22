import random
import lower_art
import game_data
import replit

# printing logo
print(lower_art.logo)

# taking the inputs
compare_a=random.choice(game_data.data)
compare_b=random.choice(game_data.data)

# function to check the two inputs
def check_inputs(A,B,d):
    print(f"compare A: {A['name']},{A['description']},{A['country']}")
    print(lower_art.vs)
    print(f"Against B: {B['name']}, {B['description']}, {B['country']}")
    choice=input("Who has more followers? Type 'A' or 'B': ")
    if choice.upper()=='A':
        dict_A(a=A,b=B,c=d)
    elif choice.upper()=="B":
        dict_B(a=B,b=A,c=d)
    else:
        print("choice is not given correct")    


# function for checking of A       
def dict_A(a,b,c):
    if a["follower_count"]>=b["follower_count"]:
        c+=1
        C=b
        check_inputs(A=C,B=random.choice(game_data.data),d=c)
    else:
        replit.clear()
        print(f"you loose with {c} points")
        
# function for checking of b    
def dict_B(a,b,c):
    if b["follower_count"]>=a["follower_count"]:
        c+=1
        C=a
        check_inputs(A=C,B=random.choice(game_data.data),d=c)
    else:
        replit.clear()
        print(f"you loose with {c} points") 

# calling function check_inputs()

check_inputs(A=compare_a,B=compare_b,d=0)



# encountered a new error where the name of the dictionary called in a function can't be called with a function name.




