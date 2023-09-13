# learnings
#  reference a dictionary and its items by dictName["key"]["value"]

"""
print(f"Here's your {get_input()} + ☕")
# resources =get_input()
print(f"{MENU[get_input()]['ingredients']['water']} ml")
"""

from menu import MENU, resources

print(MENU["latte"]["ingredients"])
print(MENU["latte"])
print(MENU)