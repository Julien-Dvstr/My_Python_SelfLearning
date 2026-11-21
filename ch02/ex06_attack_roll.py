# Roll the dice - 21/11/26

MENU_WIDTH = 20
MAX_DICE_VALUE = 20
NATURAL_TWENTY = 20
NATURAL_ONE = 1
ENEMY_DEFENSE = 10
PLAYER_ATTACK = 5
PLAYER_WEAPON_ATTACK = 2

menu_bar1 = "=" * MENU_WIDTH
menu_bar2 = "-" * MENU_WIDTH

print(f'''
{menu_bar1}
{"Player":^{MENU_WIDTH}}
{"Stats":^{MENU_WIDTH}}
{menu_bar2}
{f"Attack : {PLAYER_ATTACK}":^{MENU_WIDTH}}
{f"Weapon Damage: {PLAYER_WEAPON_ATTACK}":^{MENU_WIDTH}}
{menu_bar1}

{menu_bar1}
{"Enemy":^{MENU_WIDTH}}
{"Stats":^{MENU_WIDTH}}
{menu_bar2}
{f"Defense : {ENEMY_DEFENSE}":^{MENU_WIDTH}}
{menu_bar1}
''')

artificial_roll = int(input("D20 roll : "))
total_roll = artificial_roll + PLAYER_ATTACK + PLAYER_WEAPON_ATTACK
damage = total_roll - ENEMY_DEFENSE
if artificial_roll > MAX_DICE_VALUE:
    print("YOU ARE CHEATING !")
elif artificial_roll == NATURAL_ONE:
    print("CRITICAL FAILURE!")
    print("You lose.")
elif artificial_roll == NATURAL_TWENTY:
    print("CRITICAL SUCCESS!")
    print("You won!")
elif total_roll > ENEMY_DEFENSE:
    print(f"Your total = {total_roll} (D20:{artificial_roll} + Attack:{PLAYER_ATTACK} + Weapon:{PLAYER_WEAPON_ATTACK})")
    print(f"Enemy total = {ENEMY_DEFENSE}")
    print(f"That's a hit ! {damage} damage!")
elif total_roll < ENEMY_DEFENSE:
    print(f"Your total = {total_roll} (D20:{artificial_roll} + Attack:{PLAYER_ATTACK} + Weapon:{PLAYER_WEAPON_ATTACK})")
    print(f"Enemy total = {ENEMY_DEFENSE}")
    print(f"That's a miss !")