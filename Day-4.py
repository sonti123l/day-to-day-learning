import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
signs_list=[rock,paper,scissors]
user_choice=int(input("what do you choose? type 0 for rock,1 for paper or 2 for scissors.\n"))
computer_choice=random.choice(signs_list)
print("my choice is:")
print(signs_list[user_choice])
print("computer choice is:")
print(computer_choice)
if user_choice==signs_list.index(computer_choice):
  print("the game is draw.")
elif user_choice==0 and signs_list.index(computer_choice)==1:
  print("you lost the game!.")
elif user_choice==1 and signs_list.index(computer_choice)==2:
  print("you lost the game!.")
elif user_choice==2 and signs_list.index(computer_choice)==0:
  print("you lost the game!.")
else:
  print("you win the Game!")  
