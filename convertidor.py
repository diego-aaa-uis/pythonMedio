def conversor(tipo_peso, valor_dolar):
    pesos = input("Ingre la cantidad de dinero en pesos" + tipo_peso +" :" )
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares) 
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas 🤑

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """
opcion = input(menu )


if opcion == '1':
    conversor("colombianos",3980)
elif opcion == '2':
    conversor("argentinos", 65)
elif opcion == '3':
    conversor("mexicano", 24)
else:
    print("Ingresa una opcion correcta por favor")



