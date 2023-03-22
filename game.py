from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-","/","*"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
Incorrecto = 0
correcto = 0
for i in range(0, times):
# Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    
    if operator == "*":
        resultado = number_1 * number_2
    else:    
        if operator == "-":
            resultado = number_1 - number_2
        else:
            if operator == "+":
                resultado = number_1 + number_2
            else:
                while number_2 == 0: 
                    number_2 = randrange(10)
                resultado = number_1 / number_2
                
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = int(input("resultado: "))
    if  result == resultado: 
        print ("Correcto")
        correcto += 1
    else: 
        print ("Incorrecto")
        Incorrecto += 1
    # Al terminar toda la cantidad de cuentas por resolver.
    # Se vuelve a tomar la fecha y la hora.
    end_time = datetime.now()
    # Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"Resultados correctos: {correcto} ")
print(f"Resultados incorrectos: {Incorrecto}")
