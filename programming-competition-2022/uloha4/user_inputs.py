#!/usr/bin/python


def get_user_inputs():
    user_input: str = input("Zadaná písmena: ")

    # get usre input (letters)
    if len(user_input) > 10:
        user_input = user_input[:10]

    # get words from dictionary
    path_to_dictionary: str = input(
        "Zadejte cestu ke slovníku (výchozí je `./slovnik.txt`): ")

    return user_input, path_to_dictionary
