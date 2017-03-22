import string

def alphabet_position(letter):
    letter = letter.lower()
    return list(string.ascii_lowercase).index(letter)

def rotate_character(char, rot):

    for i in char:
        if i in string.ascii_lowercase:
            pos = (alphabet_position(i) + rot) % len(string.ascii_lowercase)
            return string.ascii_lowercase[pos]
        elif i in string.ascii_uppercase:
            pos = (alphabet_position(i) + rot) % len(string.ascii_uppercase)
            return string.ascii_uppercase[pos]
        else:
            return i

def encrypt(text, rot):
    new_text = ''
    for i in text:
        new_text += rotate_character(i, rot)
    return new_text
