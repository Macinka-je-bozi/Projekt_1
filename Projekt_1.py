"""
projekt_1.py: první projekt do Engeto Datová analýza s Pythonem

author: Marcela Trávníčková
email: travnickovamarcela@gmail.com
discord: Marcela T. (pan.maca)
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive
topographic feature that rises sharply some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet above sea level. The butte is located 
just north of US 30N and the Union Pacific Railroad, which traverse the valley.
''','''At the base of Fossil Butte are the bright red, purple, yellow and gray 
beds of the Wasatch Formation. Eroded portions of these horizontal beds slope 
gradually upward from the valley floor and steepen abruptly. Overlying them and 
extending to the top of the butte are the much steeper buff-to-white beds of 
the Green River Formation, which are about 300 feet thick.''','''The monument 
contains 8198 acres and protects a portion of the largest deposit of freshwater
fish fossils in the world. The richest fossil fish deposits are found in 
multiple limestone layers, which lie some 100 feet below the top of the butte. 
The fossils represent several varieties of perch, as well as other freshwater 
genera and herring similar to those in modern oceans. Other fish such as 
paddlefish, garpike and stingray are also present.'''
]

user_password = {
    "bob":"123",
    "ann":"pass123",
    "mike":"password123",
    "liz":"pass123"}
line = ("-"*50)

username = input("Please enter your username: ").lower()
if username not in user_password.keys():
    print("You entered wrong username, terminating the program...")
    exit()

password = input("Please enter your password: ").lower()
if password != user_password[username]:
    print("You entered wrong password, terminating the program...")
    exit()

print(line+f"\nWelcome to the app,{username}"
           "\nWe have 3 texts to be analyzed.\n"+line)
choosing_text = input("Enter a number between 1 and 3 to select text: ")
if not choosing_text.isdigit():
    print("You did not enter a number, terminating the program...")
    exit()
else:
    choosing_text = int(choosing_text)
    if choosing_text >= 4:
        print("You did not enter a number between 1 to 3, "
        "terminating the program...")
        exit()

print(line)
chosen_text = TEXTS[choosing_text-1]
words = chosen_text.split()
upper, all_upper, all_lower, numbers, number = 0, 0, 0, 0, 0
for word in words:
    if word[0].isupper():
        upper += 1
    elif word.isupper():
        all_upper += 1
    elif word.islower():
        all_lower += 1
    elif word.isdigit():
        numbers += 1
        number += int(word)

word_length = {}
for word in words:
    length = len(word.strip(".,"))
    if length in word_length.keys():
        word_length[length] += 1
    else:
        word_length[length] = 1

print(f"There are {len(words)} words in the selected text.")
print(f"There are {upper} titlecase words.")
print(f"There are {all_upper} uppercase words.")
print(f"There are {all_lower} lowercase words.")
print(f"There are {numbers} numeric strings.")
print(f"The sum of all the numbers is {number}.")

print(line+f"\n{'LEN|':<6}{'OCCURENCES':<16}|NR.\n"+line)
for i in sorted(word_length):
    stars = word_length.get(i) * "*"
    print(f"{i:3}|{stars:18}|{word_length.get(i)}")
print(line+f"\nThank you, bye {username}!\n"+line)