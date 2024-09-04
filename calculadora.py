import time

print('Elije que operador quieres seleccionar, introduciendo el numero de la operador que quieras')

print(" ")

print("1. Suma\n2. resta\n3. multiplicacion\n4. Division")

print(" ")

operacion_seleccionada = input("Introduce que operador quieres seleccionar: ")

num_1 = int(input("Pon el primer numero que quieras operar: "))

num_2 = int(input("Pon el segundo numero que quieras operar: "))


if operacion_seleccionada == "1":

    resultadoFinal= num_1 + num_2

    print("El resultado de esta operacion es: " + str(resultadoFinal))


elif operacion_seleccionada == "2":

    resultadoFinal = num_1 - num_2

    print("El resultado de esta operacion es: " + str(resultadoFinal))

elif operacion_seleccionada == "3":

    resultadoFinal = num_1 * num_2

    print("El resultado de esta operacion es: " + str(resultadoFinal))

elif operacion_seleccionada == "4":

    if num_2 != 0:

            resultadoFinal = num_1 / num_2

            print("El resultado de esta operacion es: " + str(resultadoFinal))

    else:
         
         print("Error no se puede dividir por 0")

else:

    print("Por favor verifique si introdujo el dato correctamente, Por favor seguier las instrucciones.")


print("La calculadora se cerrara en 5 segundo")

time.sleep(5)






