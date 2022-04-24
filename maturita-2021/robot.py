from copy import copy
from tkinter import *
from turtle import width
from PIL import ImageTk, Image


class Robot:
    location = [0, 0]
    directions = ["RIGHT", "UP", "LEFT", "DOWN"]
    direction = "RIGHT"
    commands_history = []
    playground = None
    rectangle = None
    images = None

    def Refresh(self):
        self.playground.Refresh()

        # delete rectangle and create new on other position
        self.playground.canvas.delete(self.rectangle)

        self.rectangle = self.playground.canvas.create_image(
            self.location[0]*40 + 20, self.location[1]*40+20,  image=self.images[self.direction])

    def Reset(self):
        self.location = [0, 0]
        self.playground.Reset()
        self.Refresh()
        self.commands_history.append("RESET")

    # rotate 90 degrees
    def Rotate(self):
        self.direction = self.directions[(
            self.directions.index(self.direction)+1) % 4]
        self.Refresh()
        self.commands_history.append("ROTATE")

    def Step(self):
        if (self.direction == "UP") and self.location[1] > 0:
            self.location[1] -= 1
        elif (self.direction == "DOWN") and (self.playground.size_y > self.location[1]+1):
            self.location[1] += 1
        elif (self.direction == "LEFT") and self.location[0] > 0:
            self.location[0] -= 1
        elif (self.direction == "RIGHT") and (self.playground.size_x > self.location[0]+1):
            self.location[0] += 1

        self.Refresh()
        self.commands_history.append("STEP")

    def Fill(self):
        self.playground.Fill(self.location[0], self.location[1])
        self.commands_history.append("FILL")
        self.Refresh()

    def Erase(self):
        self.playground.Erase(self.location[0], self.location[1])
        self.commands_history.append("ERASE")
        self.Refresh()

    def Execute(self, command):
        if command == "ROTATE":
            self.Rotate()
        elif command == "STEP":
            self.Step()
        elif command == "FILL":
            self.Fill()
        elif command == "ERASE":
            self.Fill()
        elif command == "RESET":
            self.Reset()

    def __init__(self, playground, images, location=[0, 0], commands_history=[]):
        # set location and commands_history
        self.location = location
        self.images = images
        self.commands_history = commands_history
        self.playground = playground
        self.Refresh()
