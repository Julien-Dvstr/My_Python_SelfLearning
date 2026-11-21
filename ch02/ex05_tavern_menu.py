# 21-11-26
from difflib import Match

BEER = 3
STEW = 5
ROOM = 12

MENU = f'''
----------- MENU --------------
[1] Beer {f"({BEER})":>2}
[2] Stew {f"({STEW})":>2}
[3] Room for the night {f"({ROOM})":>2}
[4] Leave
-------------------------------
'''

print('''
+=================+
|      Tavern     |
+=================+
- Welcome Adventurer !
''')

gold = int(input("- How much gold do you have ? : "))
purchase = input("- Would you like to buy something ? (y/n) : ")
match purchase:
    case "y"|"yes":
        print("- Nice ! Here is our menu !")
        print(MENU)
        menu_choice = input("What do you choose ? : ")
        match menu_choice:
            case "1"|"Beer":
                gold -= BEER
                print(f"-{BEER}g, {gold} left")
                print(f"Here is your beer !")
            case "2"|"Stew":
                gold -= STEW
                print(f"-{STEW}g, {gold} left")
                print(f"Here is your stew !")
            case "3"|"Room":
                gold -= ROOM
                print(f"-{ROOM}g, {gold} left")
                print(f"Here is your keys for the room !")
            case "4"|"Leave":
                print(f"Okay ! Thanks for your visit !")
    case "n"|"no":
        print("- Okay have a nice day !")