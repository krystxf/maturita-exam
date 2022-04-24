#!/usr/bin/python

import requests
from tkinter import *
import random
import json

server = "https://sifrovani.maturita.delta-www.cz"

def get_random_char():
    return chr(random.randint(ord('A'), ord('Z')))


def get_response(endpoint):
    response_API = requests.post(
        server + endpoint)
    return json.loads(response_API.text)


def verify(token, text, decoded_or_encoded):
    reponse_API = requests.post(
        server + "/verify", data={"token": token, decoded_or_encoded: text})

    return json.loads(reponse_API.text)["success"]
