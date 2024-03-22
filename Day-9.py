from replit import clear
#blind auction game
import art_9
print(art_9.logo)
bidders_lib={}
print("Welcome to the secret auction program")
bidders_list=[]
highest_bid=0
is_game_on='yes'
while is_game_on!='no':
    bidders_lib={}
    person=input("What is your name?: ")
    bid_amount=int(input("What's your bid?: $"))
    bidders_lib["name"]=person
    bidders_lib["money"]=bid_amount
    bidders_list.append(bidders_lib)
    continue_game=input("Anyother bidders then type 'yes',or type 'no' ")
    if continue_game=='yes': 
        is_game_on='yes'
        clear()
    else:
        is_game_on='no'
        clear()
        for list in bidders_list:
            if list["money"]>highest_bid:
                highest_bid=list["money"]
                index_value=bidders_list.index(list)
        print(f"the bidder is {bidders_list[index_value]['name']} and bid amount is {highest_bid}")                
