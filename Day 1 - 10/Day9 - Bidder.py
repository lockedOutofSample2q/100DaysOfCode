import os
os.system('cls')
bidding_dictionary={

}

more= "yes"

while more == "yes":
    ask_name = input("What's your name?: ")
    ask_bid = input("What's your bid amount?: ")
    bidding_dictionary[ask_name]= ask_bid
    more = input("Are there more players? yes/no  : ").lower()
    os.system('cls')

highest_bid = 0
for name in bidding_dictionary:
    value = int(bidding_dictionary[name]) 
    if value > highest_bid:
        highest_bid = value
        winner = name
print("winner is : " + winner + " with a bid of $" + str(highest_bid))
