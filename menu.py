from generar_password import *
from numero_caracteres import *


def menu():
    try:
        while True:      
            option = int(input(
        '''
        Escoga una opción:
          [1] Generar password.
          [2] Salir
            : '''))

            if option == 1:
                numero_caracteres = caracteres_password()
                password = generar_password(numero_caracteres)
                print_password(password)
            elif option == 2:
                print('Gracias por su visita.')
                quit()
            elif option != 1 or option != 2:
                print('Opción no válida.')
            else:
                print('Opción no válida')
        #else:
            #print('Opción no válida')
    except ValueError:
        print('Inténtalo de nuevo.')


