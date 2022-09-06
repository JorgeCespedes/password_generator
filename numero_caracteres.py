
def caracteres_password():
    
    while True:
        try:
            numero_caracteres = int(input('Ingrese el número de dígitos para generar su password: '))
        except ValueError:
            print("Debes escribir un número.")
            continue

        if numero_caracteres < 4:
            print('Ingresa un número mayor a 3 digitos.')
            continue
        else:
            break

    return numero_caracteres

