# Convertidor de monedas a dolares

menu = """
Bienvenido al Conversor de Monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos 
3 - Pesos mexicanos

Elige una opcion:  """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("pesos colombianos: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 2:
    pesos = input("pesos argentinos: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 3:
    pesos = input("pesos mexicanos: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
else:
    print("Ingrese una opcion correcta")
