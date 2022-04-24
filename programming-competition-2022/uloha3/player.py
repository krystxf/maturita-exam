#!/usr/bin/python


class Player:
    def __init__(self, sign: str, button, name: str):
        self.sign = sign
        self.button = button
        self.name = name

        self.button.config(text="Hráč %s (%s)" % (
            name, sign), width=10, state="disabled" if sign == "O" else "active")
