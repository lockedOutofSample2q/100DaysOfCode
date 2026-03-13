import recepie
import os
tank_capacity = {
       'water': 300,
        'coffee': 100,
        'milk': 200
    }


balance = {'money' : 0}
    
def coin_counter(quarter, dime, nickel, penny):
    return penny*0.01 + nickel*0.05 + dime*0.1 + quarter*0.25

def balance_report():
    print(f"Balance available : {balance['money']}")

def tank_report():
    print(tank_capacity)
    

def update_tank(water_for_order, coffee_for_order, milk_for_order):
    tank_capacity['water'] -= water_for_order
    tank_capacity['coffee'] -= coffee_for_order
    tank_capacity['milk'] -= milk_for_order

def if_missing_item(water_req,coffee_req,milk_req):
        
        if water_req<tank_capacity['water']:
            if coffee_req<tank_capacity['coffee']:
                if milk_req<tank_capacity['milk'] :
                    return False
                else:return "milk"
            else:return "coffee"
        else:return "water"

def check_tank(order, recipe):
    if order == 'espresso':
        water_req = recipe[0]['water']
        coffee_req = recipe[0]['coffee']
        milk_req = recipe[0]['milk']
        return if_missing_item(water_req,coffee_req,milk_req)


    elif order == 'latte':
        water_req = recipe[1]['water']
        coffee_req = recipe[1]['coffee']
        milk_req = recipe[1]['milk']
        return if_missing_item(water_req,coffee_req,milk_req)

    elif order == 'cappuccino':
        water_req = recipe[2]['water']
        coffee_req = recipe[2]['coffee']
        milk_req = recipe[2]['milk']
        return if_missing_item(water_req,coffee_req,milk_req)
    else:
        return order

def order_map(input_char):
    if input_char == 'e':
        return "espresso"
    elif input_char == 'l':
        return "latte"
    elif input_char == "c":
        return "cappunccino"
    else: return "invalid"

def make_coffee(check_result,coffee):
    if check_result==False:
        print(f"Here's your {coffee}, Enjoy!")
    else:
        print(f"The machine is out of {check_result}")

def cost_of_order(name):
    if name == "espresso":
        return 1.50
    if name == "latte":
        return 2.50
    if name == "cappuccino":
        return 3.00

def update_balance(new_money):
    balance['money'] += new_money

machine_state="on"
while machine_state=="on":
    print("Welcome to Hargun's PyCafe\n--------------------------\n")
    print("Coffee Menu:\n(e)Espresso         $1.50\n(l)Latte            $2.50\n(c)Cappuccino       $3.00\n\n--------------------------\n")

    order=input("Which coffee would you like?: ").lower()
    if order == "report":
        if input()=="admin":
            os.system('cls')
            tank_report()
            input("Done master?: ")
            os.system('cls')                
        else: print("Unauthorized!")
    elif order == "stock":
        if input()=="admin":
            os.system('cls')
            print(tank_capacity)
            input("Done master?: ")
            os.system('cls')                
        else: print("Unauthorized!")
    elif order == "off":
        machine_state="off"
    elif order == "balancesheet":
        if input()=="admin":
            os.system('cls')
            balance_report()
            input("Done master?: ")
            os.system('cls')                
        else: print("Unauthorized!")
    elif order_map(order) == "invalid":
        print("Invalid order!")
        break
    else:
        
        anything_missing = check_tank(order_map(order.lower()),recepie.data)
        if anything_missing==False:
            price_to_charge  = cost_of_order(order_map(order.lower()))
            ask_for_money = f"It would be {price_to_charge}"
            print(ask_for_money)
            Quarters = int(input("How many Quarters  : "))
            Dimes = int(input("How many Dimes     : "))
            Nickels = int(input("How many Nickels   : "))
            Pennies = int(input("How many Pennies   : "))
            moneygot = coin_counter(Quarters, Dimes, Nickels, Pennies)
            if moneygot >= price_to_charge:
                print(f"Here's your change of ${round(moneygot - price_to_charge,2)}")
                make_coffee(anything_missing,order_map(order).lower())
                update_balance((price_to_charge))
                
            elif moneygot < price_to_charge:
                print (f"Sorry the order costs ${round(price_to_charge - moneygot)} more")
        else:
            print(f"Sorry! Machine is out of {anything_missing}")
        

