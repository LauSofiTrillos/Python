# FUNCIONES 

def imprimir_mensaje():
    print("Mensaje especial: ")
    print("FUNCIONES")

def conversacion(mensaje):
    print("Hola")
    print(mensaje)
    print("Adios")

imprimir_mensaje()

opcion = int(input("Elige una opcion (1, 2, 3): "))
if opcion == 1:
    conversacion("Elegiste la opcion 1")
elif opcion == 2:
    conversacion("Elegiste la opcion 2")
elif opcion == 3:
    conversacion("Elegiste la opcion 3")
else:
    print("Escribe la opcion correcta")

imprimir_mensaje()
