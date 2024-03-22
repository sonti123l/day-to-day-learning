import blackjack_art
from replit import clear
import random

enter_ticket = input("Do you want to play a game of Blackjack?Type 'y' or 'n': ")

# making cards to the game.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []


# condition checking of the scores.
def score_check(your_score, machine_score):
    if your_score > 21:
        print("You're Busted!")
    elif (your_score > machine_score) and (your_score < 21):
        print("You Win!")
    elif (machine_score > your_score) and (your_score < 21):
        print("You lose,better luck next time.")
    elif (machine_score == your_score) and (your_score < 21):
        print("you're are draw")


# initial cards assigning
def have_cards():
    for card in range(2):
        user_cards.append(random.choice(cards))
    for card in range(2):
        computer_cards.append(random.choice(cards))
    return user_cards, computer_cards


# continue the game by giving the continue choice .now creating a function for it.
def make_continue(l):
    while l != 'no':
        if l == 'yes':
            user_cards = []
            computer_cards = []
            for card in range(2):
                user_cards.append(random.choice(cards))
            for card in range(2):
                computer_cards.append(random.choice(cards))
            complete_cards(my_cards=user_cards, computer_card=computer_cards)
        else:
            l = 'no'
            break

        # adding new card if needed..(if(user_score<17))


def check_condition(my_score, new_cards):
    if my_score < 17:
        new_cards.append(cards[random.randint(0, len(cards) - 1)])
        return new_cards

    # writing the conditions for the game to get working


# user_cards count.
def complete_cards(my_cards, computer_card):
    current_score = 0
    computer_score = 0
    for i in my_cards:
        current_score = current_score + i
    for j in computer_cards:
        computer_score = computer_score + j
    print(f"Your cards: {my_cards}, current score: {current_score}")
    print(f"computer's first card: {computer_card[0]}")
    user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_choice == 'y':
        card = check_condition(my_score=current_score, new_cards=user_cards)
        current_score = 0
        computer_score = 0
        for i in card:
            current_score = current_score + i
        for j in computer_cards:
            computer_score = computer_score + j
        print(f"Your cards: {card}, finalscore: {current_score}")
        print(f"computer's first card: {computer_card}, computerscore: {computer_score}")
        score_check(your_score=current_score, machine_score=computer_score)
        continue_game = input("Do you want to continue then type 'yes',or type 'no': ")
        make_continue(l=continue_game)
    elif user_choice == 'n':
        print(f"Your cards: {my_cards}, finalscore: {current_score}")
        print(f"computer's first card: {computer_card}, computerscore: {computer_score}")
        score_check(your_score=current_score, machine_score=computer_score)
        continue_game = input("Do you want to continue then type 'yes',or type 'no': ")
        make_continue(l=continue_game)


# clicking y to start
if enter_ticket == 'y':
    clear()
    print(blackjack_art.logo)
    you, computer = have_cards()
    complete_cards(my_cards=you, computer_card=computer)
else:
    print("thank you for visiting.")

# user to get the choice to continue the game.
