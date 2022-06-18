menu = """
Bienvenido al conversor de monedas 

1 - Pesos mexicanos
2 - Pesos colombianos
3 - Pesos argentinos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuantos pesos mexicanos tiene?: ")
    pesos = float(pesos)
    valor_dolar = 20.34
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 2:
    pesos = input("¿Cuantos pesos colombianos tiene?: ")
    pesos = float(pesos)
    valor_dolar = 3905.90
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 3:
    pesos = input("¿Cuantos pesos argentinos tiene?: ")
    pesos = float(pesos)
    valor_dolar = 123.16
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
else:
    print('Ingresa una opción correcta por favor')