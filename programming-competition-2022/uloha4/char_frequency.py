

def char_frequency(text):
    dict = {}
    for n in text:
        if n in dict.keys():
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
