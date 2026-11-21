# Using conditions for the first time - 19/11/26

MAX_HEALTH = 100
POTION_HP = 30
health = int(input(f"Current HP: "))
hp_healed = MAX_HEALTH-health
potion_drink = input(f"Do you want to drink a healing potion? (y/n) ")
if health < MAX_HEALTH:
    match potion_drink:
        case "y"|"yes":
            if health + POTION_HP <= MAX_HEALTH:
                health += POTION_HP
                print(f"You drink a potion. (+{POTION_HP}HP)")
                print(f"Current HP: {health}")
            elif health + POTION_HP >= MAX_HEALTH:
                print("You are going to overheal.")
                overheal = input("Do you still want to drink the potion? (y/n) ")
                match overheal:
                    case "y"|"yes":
                        print(f"You drink a potion. (+{hp_healed})")
                        health += hp_healed
                        print(f"Current HP: {health}")
                    case "n"|"no":
                        print(f"Good choice! Have a good luck out there!")
        case "n"|"no":
            print("Okay! Good luck !")
else :
    print("You are full life, good luck!")