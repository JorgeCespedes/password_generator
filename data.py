
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ] 


def letter_min(letter):
    return letter

def letter_may(letter):
    letter = [ l.upper() for l in letter ]
    return letter

def list_number(number):
    number = [ str(n) for n in number ]
    return number
