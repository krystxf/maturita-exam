#!/usr/bin/python

from tkinter import *
import threading

from skip import *
from functions import *
from grid_simple import *

# setup window
root = Tk()
root.title("Šifry")
root.geometry("600x600")
Grid.columnconfigure(root, 0, weight=1)

# UI

# frames
skip_decode_frame = Frame(root)
skip_decode_frame.grid(row=1, column=0)
skip_encode_frame = Frame(root)
grid_simple_decode_frame = Frame(root)

# SKIP
skip_decode_skip_label = Label(skip_decode_frame, text="SKIP:")
skip_decode_skip_label.grid(row=0, column=0, sticky=W)

# OFFSET
skip_decode_offset_label = Label(skip_decode_frame, text="OFFSET:")
skip_decode_offset_label.grid(row=1, column=0, sticky=W)

# ENCODED TEXT
skip_decode_encoded_text_label = Label(skip_decode_frame, text="Encoded text:")
skip_decode_encoded_text_label.grid(row=2, column=0, sticky=W)
skip_decode_encoded_text = Label(
    skip_decode_frame, text="")
skip_decode_encoded_text.grid(row=3, column=0, sticky=W)

# DECODED TEXT
skip_decode_decoded_text_label = Label(skip_decode_frame, text="Decoded text:")
skip_decode_decoded_text_label.grid(row=4, column=0, sticky=W)
skip_decode_decoded_text = Label(skip_decode_frame, text="")
skip_decode_decoded_text.grid(row=5, column=0, sticky=W)

# VALID
skip_decode_is_valid_label = Label(skip_decode_frame, text="VALID:")
skip_decode_is_valid_label.grid(row=6, column=0, sticky=W)


# SKIP
skip_encode_skip_label = Label(skip_encode_frame, text="SKIP:")
skip_encode_skip_label.grid(row=0, column=0, sticky=W)

# OFFSET
skip_encode_offset_label = Label(skip_encode_frame, text="OFFSET:")
skip_encode_offset_label.grid(row=1, column=0, sticky=W)

# ENCODED TEXT
skip_encode_encoded_text_label = Label(skip_encode_frame, text="Encoded text:")
skip_encode_encoded_text_label.grid(row=4, column=0, sticky=W)
skip_encode_encoded_text = Label(
    skip_encode_frame, text="")
skip_encode_encoded_text.grid(row=5, column=0, sticky=W)

# DECODED TEXT
skip_encode_decoded_text_label = Label(skip_encode_frame, text="Decoded text:")
skip_encode_decoded_text_label.grid(row=2, column=0, sticky=W)
skip_encode_decoded_text = Label(skip_encode_frame, text="")
skip_encode_decoded_text.grid(row=3, column=0, sticky=W)

# VALID
skip_encode_is_valid_label = Label(skip_encode_frame, text="VALID:")
skip_encode_is_valid_label.grid(row=6, column=0, sticky=W)


# SIMPLE GRID SIMPLE

simple_grid_decode_decoded_text_label = Label(
    grid_simple_decode_frame, text="Decoded text:")
simple_grid_decode_decoded_text_label.grid(row=2, column=0, sticky=W)
simple_grid_decode_decoded_text = Label(grid_simple_decode_frame, text="")
simple_grid_decode_decoded_text.grid(row=3, column=0, sticky=W)
simple_grid_decode_valid_label = Label(grid_simple_decode_frame, text="VALID:")
simple_grid_decode_valid_label.grid(row=6, column=0, sticky=W)


# DROPDOWN
dropdown_options = ("SKIP - DECODE", "SKIP - ENCODE", "GRID SIMPLE - DECODE")
clicked = StringVar()   # clicked is a variable that stores the value of the dropdown
clicked.set(dropdown_options[0])  # default value


# change frame when dropdown changes
def dropdown_change(_, __, ___):
    # skip decode
    selected_cypher = dropdown_options.index(clicked.get())
    if selected_cypher == 0:
        skip_decode_frame.grid(row=1, column=0)
    else:
        skip_decode_frame.grid_remove()

    # skip encode
    if selected_cypher == 1:
        skip_encode_frame.grid(row=1, column=0)
    else:
        skip_encode_frame.grid_remove()

    # grid simple decode
    if selected_cypher == 2:
        grid_simple_decode_frame.grid(row=1, column=0)
    else:
        grid_simple_decode_frame.grid_remove()


clicked.trace('w', dropdown_change)

dropdown = OptionMenu(root, clicked, *dropdown_options)
dropdown.grid(row=0, column=0)


def set_skip_decoded_values():
    # set everything to loading
    skip_decode_skip_label.config(text="SKIP: loading")
    skip_decode_is_valid_label.config(text="VALID: loading", fg="black")
    skip_decode_offset_label.config(text="OFFSET: loading")
    skip_decode_encoded_text.config(text="loading")
    skip_decode_decoded_text.config(text="loading")

    # get data from API
    api_response = get_response("/skip/decode")

    # set everything already loaded
    skip_decode_skip_label.config(
        text="SKIP: " + str(api_response["skip"]))
    skip_decode_offset_label.config(
        text="OFFSET: " + str(api_response["offset"]))
    skip_decode_encoded_text.config(text=api_response["encoded"])

    # decode
    decoded = decode_skip(
        api_response["skip"], api_response["offset"], api_response["encoded"])

    # set decoded text
    skip_decode_decoded_text.config(text=decoded)

    # validate
    valid = verify(api_response["token"], decoded, "decoded")

    # set valid text value
    skip_decode_is_valid_label.config(
        text="VALID: " + "True" if valid else "False", fg="green" if valid else "red")


def set_skip_encoded_values():
    # set everything to loading
    skip_encode_skip_label.config(text="SKIP: loading")
    skip_encode_is_valid_label.config(text="VALID: loading", fg="black")
    skip_encode_offset_label.config(text="OFFSET: loading")
    skip_encode_encoded_text.config(text="loading")
    skip_encode_decoded_text.config(text="loading")

    # get data from API
    api_response = get_response("/skip/encode")

    # set everything already loaded
    skip_encode_skip_label.config(
        text="SKIP: " + str(api_response["skip"]))
    skip_encode_offset_label.config(
        text="OFFSET: " + str(api_response["offset"]))
    skip_encode_decoded_text.config(text=api_response["text"])

    # encode
    encoded = encode_skip(
        api_response["skip"], api_response["offset"], api_response["text"])

    # set encoded text
    skip_encode_encoded_text.config(text=encoded)

    # validate
    valid = verify(api_response["token"], encoded, "encoded")

    # set valid text value
    skip_encode_is_valid_label.config(
        text="VALID: " + "True" if valid else "False", fg="green" if valid else "red")


def set_grid_simple_decoded_values():
    # set everything to loading
    simple_grid_decode_valid_label.config(text="VALID: loading", fg="black")
    simple_grid_decode_decoded_text.config(text="loading")

    # decode grid simple
    api_response = get_response("/grid-simple/decode")
    decoded = decode_grid_simple(
        api_response["grid"], api_response["encoded"])

    # set decoded text
    simple_grid_decode_decoded_text.config(text=decoded)

    # validate
    valid = verify(api_response["token"], decoded, "decoded")

    # set valid text value
    simple_grid_decode_valid_label.config(
        text="VALID: " + "True" if valid else "False", fg="green" if valid else "red")


def run_cypher():
    selected_cypher = dropdown_options.index(clicked.get())
    # decode skip
    if selected_cypher == 0:
        set_skip_decoded_values()

    # encode skip
    elif selected_cypher == 1:
        set_skip_encoded_values()

    elif selected_cypher == 2:
        set_grid_simple_decoded_values()


def run_click_async():
    threading.Thread(target=run_cypher).start()


# BUTTON
button_run = Button(root, text="RUN", command=run_click_async)
button_run.grid(row=0, column=1)


root.mainloop()
