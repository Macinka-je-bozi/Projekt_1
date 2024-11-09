"""
projekt_2_tic.py: druhý projekt (Tic Tac Toe) do Engeto Datová analýza s
Pythonem

author: Marcela Trávníčková
email: travnickovamarcela@gmail.com
discord: Marcela T. (pan.maca)
"""

#oddělovače, hrací pole, kontrola hry
game_field = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ",]
horizont_line = "+---"*3+"+"
vertical_line = "|"
line = "="*45
field = list(range(1,10))
games = 0
winning = [(0,1,2), (3,4,5), (6,7,8),
          (0,3,6), (1,4,7), (2,5,8),
          (0,4,8), (2,4,6)]
player_1_numbers = []
player_2_numbers = []

def show_game_field(game_field):
    print(horizont_line)
    for i in range(3):
        print(vertical_line+f"{game_field[i*3]}"+vertical_line+
              f"{game_field[i*3+1]}"+vertical_line+
              f"{game_field[i*3+2]}"+vertical_line)
        print(horizont_line)

def change_game_field_1(game_field, player_1):
    game_field[int(player_1) - 1] = " O "
    return game_field

def change_game_field_2(game_field, player_2):
    game_field[int(player_2) - 1] = " X "
    return game_field

def playing_player_1():
    player_1 = input(line + f"\n{player_1_name} | "
                            f"Please enter your move number: ")
    print(line)
    return player_1

def playing_player_2():
    player_2 = input(line + f"\n{player_2_name} | "
                            f"Please enter your move number: ")
    print(line)
    return player_2

def checking_player_1(player_1):
    if not player_1.isdigit():
        print("You have to enter a number.")
        return False
    if not int(player_1) in range(1,10):
        print("You have to enter a number between 1 and 9.")
        return False
    if not int(player_1) in field:
        print("This box is already taken.")
        return False
    else:
        return True

def checking_player_2(player_2):
    if not player_2.isdigit():
        print("You have to enter a number.")
        return False
    if not int(player_2) in range(1,10):
        print("You have to enter a number between 1 and 9.")
        return False
    if not int(player_2) in field:
        print("This box is already taken.")
        return False
    else:
        return True

#začátek, pokyny pro uživatele, vypsání prázdného hracího pole
print("Welcome to Tic Tac Toe.\n"+line)
player_1_name = input("Player 1, please enter your name: ")
player_2_name = input("Player 2, please enter your name: ")
print(line + "\nGAME RULES:\nEach player can place one mark (or stone)\n"
      "per turn on the 3x3 grid. The WINNER is who \n"
      "succeeds in placing three of their marks in a:\n"
      "* horizontal,\n* vertical or\n* diagonal row.\n"+line+
      f"\nLet's start the game, {player_1_name} and {player_2_name}!\n"+line)
show_game_field(game_field)

#smyčka hry
while True:
    #hraje hráč 1 - dává číslo, kontroluju číslo, odebírám ho z listu
    while True:
        player_1 = playing_player_1()
        if checking_player_1(player_1):
            field.remove(int(player_1))
            player_1_numbers.append(int(player_1) - 1)
            break

    #upravuju a vypisuju hrací pole po odehrání hráče 1, kontroluju hru
    game_field = change_game_field_1(game_field, player_1)
    show_game_field(game_field)
    games += 1
    for i in winning:
        if set(i).issubset(set(player_1_numbers)):
            print(line + f"\nCongratulations, {player_1_name} WON!")
            exit()
    if games == 9:
        print(line+f"\nEnd of the game. It's a draw between {player_1_name} "
                   f"and {player_2_name}!")
        exit()

    #hraje hráč 2 - dává číslo, kontroluju číslo, odebírám ho z listu
    while True:
        player_2 = playing_player_2()
        if checking_player_2(player_2):
            field.remove(int(player_2))
            player_2_numbers.append(int(player_2) - 1)
            break

    #upravuju a vypisuju hrací pole po odehrání hráče 2, kontroluju hru
    game_field = change_game_field_2(game_field, player_2)
    show_game_field(game_field)
    games += 1
    for y in winning:
        if set(y).issubset(set(player_2_numbers)):
            print(line + f"\nCongratulations, {player_2_name} WON!")
            exit()