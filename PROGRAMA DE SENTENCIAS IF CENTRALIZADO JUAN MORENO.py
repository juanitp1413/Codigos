# JUAN MORENO
# TU NOMBRE ES LARGO O CORTO
print("PROGRAMA PARA VERIFICAR LA CANTIDAD DE CARACTERES DE TU NOMBRE")
nombre= input("ingresa tu nombre: ")
if len(nombre) > 5:
    print("Tu nombre es largo")
else:
    print("Tu nombre es corto")
print("________________________________________________________________")
# NUMERO MAYOR O MENOR
print("PROGRAMA PARA IDENTIFICAR QUE NUMERO ES MAYOR")
n_1 = int(input("Ingresa el primer número: "))
n_2 = int(input("Ingresa el segundo número: "))
if n_1 > n_2:
    print("El primer número es mayor")
else:
    print("El segundo número es mayor o igual")
print("________________________________________________________________")
# MAYOR DE EDAD O MENOR DE EDAD
print("PROGRAMA PARA VERIFICAR SI ES MAYOR DE EDAD")
edad = int(input("Ingresar edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
print("________________________________________________________________")
# NUMERO POSITIVO O NEGATIVO
print("PROGRAMA PARA DETERMINAR SI UN NUMERO ES POSITIVO O NEGATIVO")
n_3 = int(input("Ingresa un número: "))
if n_3> 0:
    print("El número es positivo")
else:
    print("El número es negativo")
print("________________________________________________________________")
# IDENTIFICAR GENERO
print("PROGRAMA PARA IDENTIFICAR EL GENERO DE UNA PERSONA")
gen = input("Ingresa tu género (M para masculino, F para femenino): ")
if gen == "M":
    print("Usted es de genero masculino")
elif gen == "F":
    print("Usted es de genero femenino")
print("________________________________________________________________")
# VERIFICAR LA TEMPERATURA
print("PROGRAMA PARA VERIFICAR LA TEMPERUATURA")
temp = int(input("Ingresa la temperatura en grados Celsius: "))
if temp > 0:
    print("La temperatura es superior al punto de congelación del agua")
else:
    print("La temperatura es igual o inferior al punto de congelación del agua")
print("________________________________________________________________")
# VERIFICAR SI UN NUMERO ES PAR O IMPAR
print("PROGRAMA PARA DETERMINAR SI UN NUMERO ES PAR O IMPAR")
n_4 = int(input("Ingresa un número: "))
if n_4 % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
print("________________________________________________________________")
# VERIFICAR AÑO BISIESTO
print("PROGRAMA PARA DETERMINAR SI UN AÑO ES O NO BISIESTO")
año = int(input("Ingresa un año: "))
if (año % 4 == 0 and año % 100 != 0) :
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
print("________________________________________________________________")
# VERIFICAR HAY PALABRA PHYTON
print("PROGRAMA PARA VERIFICAR SI HAY LA PALABRA PHYTON EN UNA CADENA DE TEXTO")
cd = input("Ingresa una cadena de texto: ")
if "Python" in cd:
    print("Me encanta Python")
else:
    print("Python no encontrado😔")
print("________________________________________________________________")
# VERIFICAR NUMERO MULTIPLO DE 5
print("PROGRAMA PARA VERIFICAR SI UN NUMERO ES MULTIPLO DE 5")
n_5 = int(input("Ingresa un número: "))
if (n_5 % 5 == 0):
    print("El número es múltiplo de 5")
else:
    print("El número no es múltiplo de 5")
print("________________________________________________________________")
# VERIFICAR SI AES NIÑO ADOLESCENTE O ADULTO
print("PROGRAMA PARA VERIFICAR SI UNA PERSONA ES UN NIÑO, ADOLESCENTE O ADULTO ")
edad_2 = int(input("Ingresa tu edad: "))
if edad_2 < 12:
    print("Eres un niño")
elif 12 <= edad_2 <= 17:
    print("Eres un adolescente")
elif 18 <= edad_2:
    print("Eres un adulto")
print("________________________________________________________________")
# VERIFICAR SUMA MAYOR MENOR o IGUAL A 100
print("PROGRAMA PARA CALCULAR SI LA SUMA DE 2 NUMEROS ES MAYOR, MENOR O IGUAL A 100")
n_6 = int(input("Ingresa el primer número: "))
n_7 = int(input("Ingresa el segundo número: "))
sum= n_6 + n_7
if sum > 100:
    print("La suma es mayor a 100")
elif sum < 100:
    print("La suma es menor a 100")
elif sum == 100:
    print("La suma es igual a 100")
print("________________________________________________________________")
# VERIFICAR SI UNA CADENA ES DE 10 O MENOS CARACTERES
print("PROGRAMA PARA DETERMINAR SI UNA CADENA DE TEXTO ES LARGA O CORTA")
cad_1 = input("Ingresa una cadena de texto: ")
if len(cad_1) > 10:
    print("La cadena es larga")
else:
    print("La cadena es corta")
print("________________________________________________________________")
# VERIFICAR TU SALDO BANCARIO
print("PROGRAMA PARA CALCULAR EL SALDO BANCARIO Y TE ALCANZA EL DINERO")
saldo = int(input("Ingresa tu saldo bancario: "))
if saldo > 1000:
    print("Tienes suficiente dinero🥰")
else:
    print("Necesitas más dinero triste😔")
print("________________________________________________________________")
# VERIFICAR SI EDAD ES PRIMO
print("PROGRAMA PARA CALCULAR SI LA EDAD ES UN NUMERO PRIMO")
edad_2 = int(input("Ingresa tu edad: "))
if  (edad_2 % edad_2 == 0 ) and (edad_2 % 1 == 0) and (edad_2 % 2 !=0):
    print("Tu edad es un número primo")
else :
    print("Tu edad no es un número primo")

