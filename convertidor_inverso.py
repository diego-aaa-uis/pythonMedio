dolares = float(input("Ingresa la cantidad de dolares que tienes "))
valor = float(input("Ingresa el valor del dolar hoy en COP "))
pesos = dolares * valor
pesos = round(pesos)
pesos = str(pesos)
print("En total tienes $" + pesos + " pesos colombianos") 
