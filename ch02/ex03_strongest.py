# 21/11/26

hero1_attack = int(input("Attack of hero 1 : "))
hero2_attack = int(input("Attack of hero 2 : "))
hero3_attack = int(input("Attack of hero 3 : "))

best_attack = hero1_attack
best_hero = 1

if hero2_attack > best_attack:
    best_attack = hero2_attack
    best_hero = 2
if hero3_attack > best_attack:
    best_attack = hero3_attack
    best_hero = 3

    print(f"Hero {best_hero} is the strongest with {best_attack} attack.")