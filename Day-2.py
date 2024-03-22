# Tip calculator
print("welcome to the tip calculator")
total_bill=input("whats was the total bill? $")
percent_tip=input("what percentage tip would you like to give? 10,12,or 15? ")
people=int(input("How manu people to split the bill? "))
percent_bill=float(total_bill)*(int(percent_tip)/100)
new_total_bill=round((percent_bill+float(total_bill))/people,2)
print(f"Each person should pay: ${new_total_bill}")