# First Variable, types and f Strings - 18/11/26
# Variable
name = "Thorin"
job = "Warrior"
level = 12
health = 87
MAX_HEALTH = 120
gold = float(350.5)

# Interface
print(f'''
==== {name}, {job} ====
Level : {level}
Health : {health}/{MAX_HEALTH}
Gold : {gold:.2f}
''')

# Auto correction
assert name == "Thorin" and job == "Warrior"
assert level == 12 and health == 87 and MAX_HEALTH == 120
assert type(gold) == float