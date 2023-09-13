#coffee machine

# 3 hot falvours - expresso , latte, cappuccino

#  coin operated

#  expresso 50 ml water 18 g coffee - $1.50

# latte 200ml water, 24g coffee 150 ml milk - $2.50

# cappuccio 250ml water 24g coffee 100 ml milk - $3.00

from menu import  MENU, resources

# print(MENU)
# print(resources)


def get_input():
    coffee = input("What would you like? (espresso/latte/cappuccino) : ").lower()
    for key in MENU:
        if coffee in MENU.keys():
            return coffee

print(f"Here's your {get_input()} + ☕")
# resources =get_input()
print(f"{MENU[get_input()]['ingredients']['water']} ml")

def exit_machine():
        pass

def print_report():
    pass

def check_resources():
    pass

def process_coins():
    pass

def check_transaction():
    pass

def make_coffee():
    pass





