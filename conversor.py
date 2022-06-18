pesos = input("¿Cuantos pesos mexicanos tiene?: ")
pesos = float(pesos)
valor_dolar = 0.049
dolares = pesos / valor_dolar
dolares = roud(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")