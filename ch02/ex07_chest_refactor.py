# Upgrade the code - 21/11/26

# Original code
"""
has_key = input("Do you have the key? (y/n) ") == "y"
strength = int(input("Strength: "))
is_trapped = input("Is the chest trapped? (y/n) ") == "y"
if has_key == True:
    if is_trapped == True:
        print("The chest opens... and the trap goes off!")
    else:
        print("The chest opens. Treasure!")
else:
    if strength >= 15:
        if is_trapped == True:
            print("Thh chest opens... and the trap goes off!")
        else:
            print("The chest opens. Treasure!")
    else:
        print("The chest resists.")
"""

# My Code
has_key = input("Do you have the key? (y/n) ") == "y"
strength = int(input("Strength: "))
is_trapped = input("Is the chest trapped? (y/n) ") == "y"
if has_key or strength and is_trapped:
    print("The chest opens... and the trap goes off!")
elif has_key or strength >= 15 and not is_trapped:
    print("The chest opens. Treasure!")
else:
    print("The chest resists.")

# Solution
'''
has_key = input("Do you have the key? (y/n) ") == "y"
strength = int(input("Strength: "))
is_trapped = input("Is the chest trapped? (y/n) ") == "y"

can_open = has_key or strength >= 15

if not can_open:
    print("The chest resists.")
elif is_trapped:
    print("The chest opens... and the trap goes off!")
else:
    print("The chest opens. Treasure!")
'''