# learnings
#  reference a dictionary and its items by dictName["key"]["value"]

"""
print(f"Here's your {get_input()} + ☕")
# resources =get_input()
print(f"{MENU[get_input()]['ingredients']['water']} ml")
"""

from menu import MENU, resources

print(MENU.keys()) # just the keys
print(MENU.items()) # items as a list
print(MENU.values()) # values without keys
print(MENU["latte"]["ingredients"]["milk"]) # lowest value
print(MENU["latte"]["ingredients"]) #second lowest value
print(MENU["latte"]["cost"]) # third lowest or second highest value
print(MENU["latte"]) # highest value
print(MENU) # all items as dictionary