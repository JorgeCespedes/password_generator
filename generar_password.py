from errno import WSAEDQUOT
from data import *
import random

def generar_password(numero_caracteres):
    l  = letter_min(letter)
    lm = letter_may(letter)
    n  = list_number(number)

    tot = l + lm + n

    password = ''.join([ tot[random.randint(0, len(tot) - 1)] for i in range(numero_caracteres) ])
    
    return password


def print_password(password):
    print(' ')
    print('Your password is:')
    print('=' * (len(password) + 4))
    print('|| ', password)
    print('=' * (len(password) + 4))
    print(' ')
