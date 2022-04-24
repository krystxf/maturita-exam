

def get_user_inputs():
    gameboard_size: int = int(input("Zadejte velikost hracího pole: "
                                    ))
    # get inputs from user
    player1_sign: str = input(
        "Zadejte znak prvního hráče (vždy začíná hráč X)   (X/O): ").capitalize()
    player1_name: str = input("Zadejte jméno prvního hráče: ")
    player2_name: str = input("Zadejte jméno druhého hráče: ")

    return gameboard_size, player1_sign, player1_name, player2_name
