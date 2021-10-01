# recorrer un string 

def run():
    # cada letra de tu nombre 
    nombre = input("tu nombre: ")
    for letra in nombre:
        print(letra)

    # cada caracter de la frase en mayuscula
    frase = input("Escriba una frase: ")
    for caracter in frase:
        print(caracter.upper())

    
if __name__ == '__main__':
    run()
