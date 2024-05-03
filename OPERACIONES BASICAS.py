#OPERACIONES MATEMATICAS
a = 5 + 2 #creamos una variable que resgistre suma de numeros enteros
b = float(7.5 - 5.2) #creamos una variable que resgistre resta de numeros con punto flotante
c = 5*8 #creamos una variable que resgistre multiplicacion de enteros
d = float(8/7) #creamos una variable que resgistre division de flotantes
print("OPERACIONES MATEMATICAS")
print(f"suma enteros: {a}, resta flotantes: {b}, multiplicacion enteros: {c}, division flotantes: {d}") # imprimimos los resultados de las operaciones
#MANIPULACION DE CADENAS DE TEXTO
name = "Juanito Cato" #creamos una variable con nuestro nombre
t = len(name) #realizamos la funcion que cuenta los numeros de caracteres
print("________________________________")
print("MANIPULACION DE CADENAS DE TEXTO")
print(f"longitud del nombre es = {t}") #este codigo  sirve para contar los numeros de caracreres que tiene mi nombre
#CONVERSION DE TIPO DE DATOS
e = 8 #creamos una variable que guarde un numero entero
f = 7.5 #creamos una variable que guarde un numero con punto flontante
e1 = float(e) #creamos una variable a partir de la anterior para transformar enteros a flotantes
f1 = int(f) #creamos una variable a partir de la anterior para transformar flotantes a enteros
print("________________________________")
print("CONVERSION DE TIPO DE DATOS")
print(f"tipo original primera variable: {type(e)}, tipo convertido  {type(e1)}") #imprimimos la variable original y la variable convertida
print(f"tipo original segunda variable: {type(f)}, tipo de convertido {type(f1)}") #imprimimos la variable original y la variable convertida