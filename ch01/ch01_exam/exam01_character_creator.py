# ch01 End of chapter test - 19/11/26

# CONSTANT
BASE_GAME_WIDTH = 15
BASE_HEALTH = 50
BASE_ATTACK = 5
BASE_SPEED = 1
MAX_ATTRIBUTE_POINTS = 10
DODGE_PER_AGILITY = 4.5
SPEED_DIVISOR = 10
HEALTH_PER_STRENGTH = 8
ATTACK_PER_STRENGTH = 2
HEALTH_POWER_DIVISOR = 10
DODGE_POWER_DIVISOR = 2

# INPUT
name = input("What is your character name? : ")
title = input("What is your character title? : ")
strength = int(input("What is your character strength? (0 to 10) : "))

# CALCULATING
fullname = name + " " + title
game_width = BASE_GAME_WIDTH + len(fullname)
bar1 = "=" * game_width
bar2 = "-" * game_width

agility = MAX_ATTRIBUTE_POINTS - strength
health = BASE_HEALTH + strength * HEALTH_PER_STRENGTH
attack = BASE_ATTACK + strength * ATTACK_PER_STRENGTH
dodge = agility * DODGE_PER_AGILITY
speed = BASE_SPEED + agility / SPEED_DIVISOR
power = round(health / HEALTH_POWER_DIVISOR + attack + dodge / DODGE_POWER_DIVISOR)

left_space = game_width // 2
right_space = game_width - left_space - 1

strength_bar = "[" + "■" * strength + "." * agility + "]"
agility_bar = "[" + "■" * agility + "." * strength + "]"

# DISPLAY
print(f'''
{bar1}
#{fullname:^{game_width-2}}#
{bar1}
{"HP":<{left_space}}:{health:>{right_space}}
{"Attack":<{left_space}}:{attack:>{right_space}}
{"Dodge":<{left_space}}:{dodge:>{right_space-1},.1f}%
{"Speed":<{left_space}}:{speed:>{right_space},.2f}
{"Power":<{left_space}}:{power:>{right_space}}
{bar2}
{"Strength":<{left_space-6}}{strength_bar}{strength:>{right_space-6}}
{"Agility":<{left_space-6}}{agility_bar}{agility:>{right_space-6}}
{bar1}
''')

# Here is the correction proposed by GPT-6
"""
# Constants
BASE_GAME_WIDTH = 30
BASE_HEALTH = 50
BASE_ATTACK = 5
BASE_SPEED = 1

MAX_ATTRIBUTE_POINTS = 10
DODGE_PER_AGILITY = 4.5
SPEED_DIVISOR = 10
HEALTH_PER_STRENGTH = 8
ATTACK_PER_STRENGTH = 2
HEALTH_POWER_DIVISOR = 10
DODGE_POWER_DIVISOR = 2

# Input
name = input("Character name: ")
title = input("Character title: ")
strength = int(input("Strength (0-10): "))

# Character stats
full_name = f"{name} {title}"

agility = MAX_ATTRIBUTE_POINTS - strength
health = BASE_HEALTH + strength * HEALTH_PER_STRENGTH
attack = BASE_ATTACK + strength * ATTACK_PER_STRENGTH
dodge = agility * DODGE_PER_AGILITY
speed = BASE_SPEED + agility / SPEED_DIVISOR
power = round(health / HEALTH_POWER_DIVISOR + attack + dodge / DODGE_POWER_DIVISOR)

# Attribute bars
strength_bar = "■" * strength + "." * agility
agility_bar = "■" * agility + "." * strength

# Character sheet layout
game_width = BASE_GAME_WIDTH + len(full_name)
label_width = 12
value_width = game_width - label_width -1

border = "=" * game_width
separator = "-" * game_width

dodge_text = f"{dodge:.1f}%"
speed_text = f"{speed:.2f}"

strength_text = f"[{strength_bar}] {strength}"
agility_text = f"[{agility_bar}] {agility}"

# Display
print(f'''
{border}
#{full_name:^{game_width - 2}}#
{border}
{"HP":<{label_width}}:{health:>{value_width}}
{"Attack":<{label_width}}:{attack:>{value_width}}
{"Dodge":<{label_width}}:{dodge_text:>{value_width}}
{"Speed":<{label_width}}:{speed_text:>{value_width}}
{"Power":<{label_width}}:{power:>{value_width}}
{separator}
{"Strength":<{label_width}}:{strength_text:>{value_width}}
{"Agility":<{label_width}}:{agility_text:>{value_width}}
{border}
''')
"""