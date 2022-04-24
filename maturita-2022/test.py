#!/usr/bin/python


from skip import *
from functions import *
from grid_simple import *

# decode skip
print("DECODE SKIP")
api_response = get_response("/skip/decode")
decoded = decode_skip(
    api_response["skip"], api_response["offset"], api_response["encoded"])
print("OK" if verify(api_response["token"], decoded, "decoded") else "FAIL")


# encode skip
print("ENCODE SKIP")
api_response = get_response("/skip/encode")
encoded = encode_skip(
    api_response["skip"], api_response["offset"], api_response["text"])
print("OK" if verify(api_response["token"], encoded, "encoded") else "FAIL")


# decode grid simple
print("DECODE GRID SIMPLE")
api_response = get_response("/grid-simple/decode")
decoded = decode_grid_simple(api_response["grid"], api_response["encoded"])
print("OK" if verify(api_response["token"], decoded, "decoded") else "FAIL")

# decode grid simple

print("ENCODE GRID SIMPLE")
api_response = get_response("/grid-simple/encode")
encoded = encode_grid_simple(api_response["grid"], api_response["text"])
print("OK" if verify(api_response["token"], encoded, "encoded") else "FAIL")
