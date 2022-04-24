#!/usr/bin/python


from char_frequency import char_frequency
from user_inputs import get_user_inputs

user_input, path_to_dictionary = get_user_inputs()

dictionary: list = open("./slovnik.txt" if path_to_dictionary ==
                        "" else path_to_dictionary, 'r').read().splitlines()

# all words containing letters
correct_words: list = []


# find longest word that can be created from user_input letters
for word in dictionary:
    if len(word) > len(user_input):
        continue
    char_freq_user = char_frequency(user_input.capitalize())
    char_freq_word = char_frequency(word.capitalize())

    # check if word can be created from user_input letters

    is_ok = True
    for letter in char_freq_word:
        # check if user input contains all letters from word
        if not(letter in char_freq_user and char_freq_user[letter] >= char_freq_word[letter]):
            print(word)
            is_ok = False
    if is_ok:
        correct_words.append(word)

# find longest word in list
longest_word: str = ""
for word in correct_words:
    if len(word) > len(longest_word):
        longest_word = word


if correct_words == []:
    print("Žádné takové slovo neexistuje")
else:
    print(longest_word)
