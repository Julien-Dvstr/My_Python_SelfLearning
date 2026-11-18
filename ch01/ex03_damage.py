# Wright code for the instruction - 18/11/26
# Ask the player for their weapon's power (integer) and then the critical multiplier (decimal, e.g., 1.5).
# Display the normal damage, the critical damage rounded to the nearest integer, and the difference.

weapon_power = int(input("What is the power of your weapon ? : "))
critical_multiplier = float(input("What is the critical multiplier ? : "))
critical_damage = round(weapon_power * critical_multiplier)
print(f'''
==== Weapon Menu ====
Weapon Power : {weapon_power}
Critical Multiplier : {critical_multiplier}
------------------
Normal Damage : {weapon_power}
Critical Damage : {critical_damage}
Critical Bonus : {critical_damage - weapon_power}
''')