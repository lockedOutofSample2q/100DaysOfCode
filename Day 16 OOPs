OOPS basics


from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

isOn = True
while isOn:
    print(menu.get_items())
    choice = input(f"What would you like to have({menu.get_items()}): ")
    if choice == "report":
        money_machine.report()
        coffee_maker.report()
    elif choice == "off":
        break
    elif choice in menu.get_items():
        item = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)
            else: 
                print("Insufficient amount!")
        else: print("insufficient resources available!")
    else:
        print("Invalid order!")
