#Step 1
import random
import hangman
import hangmun_art

print(hangmun_art.logo)
choosen_word=random.choice(hangman.word_list)

choosen_word_list=[]

for word in choosen_word:
    choosen_word_list.append("_")  
    
end_of_game=False

lives=6

while end_of_game!=True:
    user_guess=input("Guess a letter: ")
    for i in range(len(choosen_word)):
        if user_guess==choosen_word[i]:
            choosen_word_list[i]=user_guess 
    print(" ".join(choosen_word_list))                 
    if user_guess not in choosen_word:
        if lives==0:
            end_of_game=True
            print(hangmun_art.stages[lives])
            print("You have lost")
        else:
            print(hangmun_art.stages[lives])
            lives-=1    
               
    if choosen_word_list.count("_")==0:
        print("You Win!")
        end_of_game=True
    else:
        print()    



        

  
   