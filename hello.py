#coffee machine

# 3 hot falvours - expresso , latte, cappuccino

#  coin operated

#  expresso 50 ml water 18 g coffee - $1.50

# latte 200ml water, 24g coffee 150 ml milk - $2.50

# cappuccio 250ml water 24g coffee 100 ml milk - $3.00

from menu import  MENU, resources

# print(MENU)
# print(resources)

coffee = input("What would you like? (espresso/latte/cappuccino) : ").lower()

def get_input():
    for key in MENU:
        if coffee in MENU.keys():
            return coffee
        elif coffee =='report':
            print("running report")
        elif coffee =='off':
            print('Turning off and resetting')
        else:
            get_input()

coffee_cost= MENU[coffee]['cost']
print(f"Here's your ☕. The cost will be ${coffee_cost:.2f}")
print(f"Input coins to the value of at least ${coffee_cost:.2f}")

# resources =get_input()
print(f"Water needed = {MENU[get_input()]['ingredients']['water']} ml")
if coffee !='espresso':
    print(f"Milk needed = {MENU[get_input()]['ingredients']['milk']} ml")
print(f"Coffee needed = {MENU[get_input()]['ingredients']['coffee']} gr")

def exit_machine():
        pass

def print_report():
    pass

def check_resources():
    pass

def process_coins(coffee_cost):
    pass

def check_transaction():
    pass

def make_coffee():
    pass





