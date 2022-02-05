#Una lista de todos los múltiplos de cuatro, de 6 y de 9, hasta 5 dígitos

listaNumeros = [i for i in range(1,100000) if i % 4==0 and i % 6 == 0 and i % 9 == 0]

print(listaNumeros)