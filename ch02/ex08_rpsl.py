# Rock, paper, scissors and lizard - 21/11/26

MENU_WIDTH = 20
BAR1 = "#" * MENU_WIDTH
BAR2 = "-" * MENU_WIDTH
PLAYER_ONE_WIN = "Player 1 win!"
PLAYER_TWO_WIN = "Player 2 win!"
MENU = f"""
{BAR1}
{"Welcome!":^{MENU_WIDTH}}
{BAR2}
{"[1] Rock"}
{"[2] Paper"}
{"[3] Scissor"}
{"[4] Lizard"}
{BAR1}
"""
rock = 1
paper = 2
scissors = 3
lizard = 4

print(MENU)
player1 = int(input("Player 1: "))
player2 = int(input("Player 2: "))

if player1 < 1 or player1 > 4 or player2 < 1 or player2 > 4:
    print("Please choose a number between 1 and 4.")
elif player1 == player2:
    print("That's a draw !")
elif player1 == rock and (player2 == scissors or player2 == lizard):
    print(PLAYER_ONE_WIN)
elif player1 == paper and player2 == rock:
    print(PLAYER_ONE_WIN)
elif player1 == scissors and (player2 == paper or player2 == lizard):
    print(PLAYER_ONE_WIN)
elif player1 == lizard and player2 == paper:
    print(PLAYER_ONE_WIN)
else:
    print(PLAYER_TWO_WIN)