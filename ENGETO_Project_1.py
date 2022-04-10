"""
author = Peter Kubovcik
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

reg_users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# init. variables
separator = "-"*40
title_words, upper_words, lower_words = 0, 0, 0
num_strings = []
words_dict = {}

# login
username = input("username")
password = input("password")
if (username, password) in reg_users.items():
    print(separator, 'Welcome to the app, ' + username, 'We have 3 texts to be analyzed.', separator, sep='\n')
else:
    print("unregistered user, terminating the program..")
    quit()

# choice of text
txt_choice = input("Enter a number btw. 1 and 3 to select: ")
if not txt_choice.isnumeric() or int(txt_choice) not in range(1, 4):
    print("wrong number, terminating the program..")
    quit()

# stats - no. of words
split_text = (TEXTS[int(txt_choice)-1]).split()
clean_words = [word.strip(".,-:!?") for word in split_text]
print(f'There are {len(split_text)} words in the selected text.')

# stats - titlecase words, uppercase, lowercase, number strings, sum of numbers
for clean_word in clean_words:
    for letter in clean_word[0]:
        if letter.isupper():
            title_words += 1
    if clean_word.isupper() and clean_word.isalpha():
        upper_words += 1
    elif clean_word.islower():
        lower_words += 1
    elif clean_word.isnumeric():
        num_strings.append(int(clean_word))
print(f'There are {title_words} titlecase words.')
print(f'There are {upper_words} uppercase words.')
print(f'There are {lower_words} lowercase words.')
print(f'There are {len(num_strings)} numeric strings.')
print(f'The sum of all numbers {sum(num_strings)}.')

# stats - occurrences
for clean_word in clean_words:
    length_word = len(clean_word)
    if length_word not in words_dict:
        words_dict[length_word] = 1
    else:
        words_dict[length_word] += 1
sorted_dict = {key: words_dict[key] for key in sorted(words_dict.keys())}
print(separator)
print(f'{"LEN":>3}|{"OCCURRENCES":^18}|{"NR.":<3}')
print(separator)
for x, y in sorted_dict.items():
    print(f'{x:>3}|{(y*"*"):<18}|{y:<3}')