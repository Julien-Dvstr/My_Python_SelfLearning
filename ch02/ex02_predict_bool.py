# Predict the next code - 21/11/26

gold = 0
name = "Kael"
has_sword = True
level = 7
print(gold > 0 or has_sword)                #True
print(not has_sword and level > 5)          #False
print(bool(name), bool(gold), bool(""))     #True, False, False
print(5 < level <= 7)                       #True
if gold:
    print("rich")                           #
elif name:
    print("poor but named")                 #poor but named
else:
    print("nothing")                        #
match level:
    case 1 | 2 | 3:
        print("beginner")
    case n if n >= 5:
        print("veteran",n)                  #veteran
    case _:
        print("intermediate")