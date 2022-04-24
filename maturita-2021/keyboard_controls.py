# keyboard controls
def keypress(event, player):
    # vim controls and WASD
    if event.char == "q":
        player.Step()
    elif event.char == "w":
        player.Rotate()
    elif event.char == " ":
        if player.playground.array[player.location[0]][player.location[1]] == "empty":
            player.Fill()
        else:
            player.Erase()
