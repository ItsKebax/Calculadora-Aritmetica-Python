import time

print('Elije que operador quieres seleccionar, introduciendo el numero de la operador que quieras')

print(" ")

print("1. Suma\n2. resta\n3. multiplicacion\n4. Division")

print(" ")

operacion_seleccionada = input("Introduce que operador quieres seleccionar: ")

def function_num1():

    input_num1= int(input("Pon el primer numero que quieras operar: "))

    return input_num1

def function_num2():

    input_num2= int(input("Pon el segundo numero que quieras operar: "))

    return input_num2
 
num_1 = function_num1()

num_2 = function_num2()

if operacion_seleccionada == "1":

    resultado_final = num_1 + num_2

    print("El resultado de esta operacion es: " + str(resultado_final))


elif operacion_seleccionada == "2":

    resultado_final = num_1 - num_2

    print("El resultado de esta operacion es: " + str(resultado_final))

elif operacion_seleccionada == "3":

    resultado_final = num_1 * num_2

    print("El resultado de esta operacion es: " + str(resultado_final))

elif operacion_seleccionada == "4":

    if num_2 != 0:

            resultado_final = num_1 / num_2

            print("El resultado de esta operacion es: " + str(resultado_final))

    else:
         
         print("Error no se puede dividir por 0")

else:

    print("Por favor verifique si introdujo el dato correctamente, Por favor seguier las instrucciones.")


print("La calculadora se cerrara en 5 segundo")

time.sleep(5)








