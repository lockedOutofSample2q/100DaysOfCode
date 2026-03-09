import random
cards = {
    "A" : [1,11],
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6,
    7 : 7,
    8 : 8,
    9 : 9,
    10 : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10
}

def draw_card():
    return random.choice(list(cards.keys()))

tally = {
    "player" : [],
    "dealer" : [],
}

def sum(tally):
    player_sum = 0
    dealer_sum = 0
    for card in tally["player"]:
        if card == "A":
            if player_sum + 11 > 21:
                player_sum += 1
            else:
                player_sum += 11
        else:
            player_sum += cards[card]
    
    for card in tally["dealer"]:
        if card == "A":
            if dealer_sum + 11 > 21:
                dealer_sum += 1
            else:
                dealer_sum += 11
        else:
            dealer_sum += cards[card]
    
    return [player_sum, dealer_sum]

def hit():
    tally["player"].append(draw_card())
  
def stand():
    tally["dealer"].append(draw_card())

def add_balance(amount):
    global bet_balance
    bet_balance += amount

print("Welcome to Py-BlackJack!")
yes_no = input("Let's deal the cards!(y/n)")

bet_amount = int(input("How much do you want to bet?: "))
bet_balance = 0

if bet_amount > bet_balance:
    print("You don't have enough balance to make that bet. Please add more funds.")
    additional_amount = int(input("How much do you want to add to your balance?: "))
    add_balance(additional_amount)
    print(f"Your current balance is: {bet_balance} dollars.")
    bet_amount = int(input("How much do you want to bet?: "))
    bet_balance -= bet_amount


if yes_no.lower() == "y":
        
        tally["player"].append(draw_card())
        tally["player"].append(draw_card())
        tally["dealer"].append(draw_card())
        print(tally)
        print(sum(tally))
        while yes_no.lower() == "y":
            while sum(tally)[0]<21 or sum(tally)[1]<21 or bet_balance == 0:
                choice = input("Do you want to hit or stand? (h/s)").lower()
                if choice =='h':
                    hit()
                    print(tally)
                    print(sum(tally))
                    if sum(tally)[0] > 21:
                        print("You busted! Dealer wins.")
                        print(f"Your current balance is: {bet_balance} dollars.")
                        break
                    if sum(tally)[0] == 21:
                        print(f"Congratulations! You win! {2*bet_amount} dollars have been added to your balance.")
                        bet_balance += 2 * bet_amount
                        print(f"Your current balance is: {bet_balance} dollars.")
                        break
                if choice == "s":
                    while sum(tally)[1] <= 21:
                        stand()
                        print(tally)
                        print(sum(tally))
                    if sum(tally)[1] > 21:
                        print(f"Dealer busted! You win! {2*bet_amount} dollars have been added to your balance.")
                        bet_balance += 2 * bet_amount
                        print(f"Your current balance is: {bet_balance} dollars.")
                        break
                    if sum(tally)[1] == 21 or sum(tally)[1] > sum(tally)[0]:
                        print("Dealer wins with a blackjack!")
                        print(f"Your current balance is: {bet_balance} dollars.")
                        break
            yes_no = input("Let's deal again? (y/n)")  
            bet_amount = int(input("How much do you want to bet?: "))
            bet_balance -= bet_amount
                     
else: print ("Okay bye!")