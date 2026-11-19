# Make operation to calculate money (1 gold = 100 silver, 1 silver = 100 copper) - 19/11/26

total_copper = 1234567

gold = total_copper // 10000
rest = total_copper % 10000
silver = rest // 100
copper = rest % 100

print(f"Fortune : {gold} gold, {silver} silver, {copper} copper")

assert gold == 123 and silver == 45 and copper == 67
assert gold * 10000 + silver * 100 + copper == total_copper