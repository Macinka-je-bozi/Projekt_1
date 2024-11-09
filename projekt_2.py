"""
projekt_2.py: druhý projekt (Bulls and Cows) do Engeto Datová analýza s
Pythonem

author: Marcela Trávníčková
email: travnickovamarcela@gmail.com
discord: Marcela T. (pan.maca)
"""
import random

#generuju náhodné čtyřmístné číslo (unikátní číslice, nezačíná nulou)
def generate_number():
    numbers = list(range(1,10))
    secret_number = []
    for i in range(4):
        number = random.choice(numbers)
        if i == 0:
            numbers.append(0)
        secret_number.append(str(number))
        numbers.remove(number)
    return secret_number

#získávám číslo od uživatele
def get_number():
    getting_number = True
    while getting_number:
        print(line)
        number = input("Enter a number: ")
        print(line)
#kontroluju, aby to číslo bylo hratelné
        if not number.isdigit():
            print("Sorry, you did not enter a number.\n"+try_again)
        elif len(number) < 4:
            print("Sorry, you entered number of less than 4 digits.\n"+
                  try_again)
        elif len(number) > 4:
            print("Sorry, you entered number of more than 4 digits.\n"+
              try_again)
        elif number.startswith('0'):
            print("Sorry, you entered number which starts with 0.\n"+try_again)
        elif len(set(number)) != 4:
            print("Sorry, you entered number which has not 4 unique digits.\n"+
              try_again)
        else:
            print(">>>", number)
            guessed_number = list(number)
            return guessed_number

#začátek, pokyny uživateli
line = ("-"*50)
print("Hi there!\n"+line,
      "\nI've generated a random 4 digit number for you.\n"+
      "Let's play a bulls and a cows game.\n"+
      "You will be guessing the generated random number\n"+
      "so you have to enter a number of 4 unique digits.")
try_again = "Please try again."
guess = 0

#vygenerování náhodného čísla
secret_number = generate_number()

#smyčka se získáním čísla od uživatele a hrou
while True:
    guessed_number = get_number()
    guess += 1
    bulls = 0
    cows = 0
    if guessed_number == secret_number:
        print(f"Correct, you've guessed the right number in {guess} guesses!"
              f"\n"+line+"\nThat's amazing!")
        exit()
    else:
        for i in range(len(guessed_number)):
            if guessed_number[i] in secret_number:
                if guessed_number[i] == secret_number[i]:
                    bulls += 1
                else:
                    cows += 1
        print(f"{bulls} {'bull'if bulls == 1 else 'bulls'},"+
            f"{cows} {'cow'if cows == 1 else 'cows'}")
