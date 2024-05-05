#UNIVERSIDAD CATOLICA DE CUENCA
#JUAN MORENO
#SISTEMAS BIOMEDICOS
#1. REGISTRO DE PACIENTES
print("↗↗ RECOLECCIÓN DE DATOS BIOMÉDICOS ↖↖")
print("______________________________________________________________________________")
print("↗↗ REGISTRO DEL PACIENTE ↖↖")
print("______________________________________________________________________________")
#pedimos que ingrese el nombre y lo guardamos en una variable str
nombre =   input("Ingrese sus nombres por favor   |→ ")
#pedimos que ingrese el apellido y lo guardamos en una variable str
apellido = input("Ingrese sus apellidos por favor |→ ")
#pedimos que ingrese la edad y la guardamos en una variable int
edad = int(input("Ingrese su edad por favor       |→ "))
#pedimos que ingrese el genero y lo guardamos en una variable str
genero =   input("Ingrese su género por favor (m/f) masculino/femenino     |→ ")
#creamos una lista con todos los datos del paciente
d_paciente = [nombre, apellido, edad, genero]
print("______________________________________________________________________________")
#2.REGISTRO DE SIGNOS VITALES
print("↗↗ REGISTRO DE SIGNOS VITALES ↖↖")
#pedimos que ingrese la temperatura corporal y la guardamos en una variable float
tc_paciente = float(input("Ingrese su temperatura corporal por favor        |→ "))
#pedimos que ingrese la presion arterial sistolica y la guardamos en una variable int
pa_sistolica =  int(input("Ingrese su presión arterial sistólica por favor  |→ "))
#pedimos que ingrese la presion arterial diastolica y la guardamos en una variable int
pa_diastolica = int(input("Ingrese su presión arterial diastólica por favor |→ "))
#pedimos que ingrese los latidos por minuto y lo guardamos en una variable int
l_min =         int(input("Ingrese sus latidos por minuto por favor         |→ "))
#creamos una lista con todos los signos vitales
sv_paciente = [tc_paciente, pa_sistolica, pa_diastolica, l_min]
print("______________________________________________________________________________")
#3.CALCULOS DE SALUD
print("↗↗ CALCULOS DE SALUD ↖↖")
#pedimos que ingrese la altura en centimetros y la guardamos en una variable float
altura = float(input("Ingrese su altura en centimetros por favor |→ "))
#pedimos que ingrese  el peso en kilogramos y lo guardamos en una variable float
peso   = float(input("Ingrese su peso en kilogramos por favor    |→ "))
#convertirmos la altura de centrimetros a metros
altura =(altura/100)
#calculamos el indice de masa muscular con la siguiente formula y redondeamos el valor del ICM en un decimal
IMC = round(peso / (altura*altura),1)
#calculamos la frecuancia cardiaca maxima con la siguiente formila
FCM = float(220-edad)
#calculamos la presion arterial media con la siguiente formula
PAM = float((pa_sistolica + (2*pa_diastolica)) / 3)
#redondeamos el valor de la presion arterial media en un valor de un decimal
PAM = round(PAM,1)
#creamos una lista donde guarde todos los calculos de salud
c_salud = [IMC, FCM, PAM]
print("______________________________________________________________________________")
print("↗↗ REGISTRO DE MEDICIONES CONTINUAS ↖↖")
#preguntamos si tiene alguna enfermedad catastrofica
print("_________________________")
en_pregunta = input("¿Usted presenta enfermedades catastroficas? (si/no) |→ ")
#con el condicional if definimos que si escoge que si damos paso a que ingrese la enfermedad y la guardamos en una variable str
if en_pregunta == "si":
    enfermedad = input("Ingrese su enfermedad por favor  |→ ")
#si escoge que no definimos la variable enfermedad como "nada"
else:
    enfermedad = "Nada"
print("_________________________")
#preguntamos si tiene alguna alergias
al_pregunta = input("¿Usted presenta alegrias a algun medicamento? (si/no) |→ ")
#con el condicional if definimos que si escoge que si damos paso a que ingrese la alergia y la guardamos en una variable str
if al_pregunta == "si":
    alergia = input("Ingrese su alergia por favor  |→ ")
#si escoge que no definimos la variable alergia como "nada"
else:
    alergia = "Nada"
print("_________________________")
#pedimos que ingrese informacion adicional importante de mencionar
adicional = input("Ingrese alguna condicion que crea importante de mencionar |→ ")
#creamos una lista donde guarde toda la informacion de mediciones continuas
mediciones = [enfermedad, alergia, adicional]
#imprimimos todos los datos anteriormente calculados e ingresados
print("______________________________________________________")
print("↘ DATOS DEL PACIENTE ↙")
print("")
print(f"Nombre completo| {d_paciente[0]} {d_paciente[1]}")
print(f"Edad|   {d_paciente[2]}")
print(f"Género| {d_paciente[3]}")
print("______________________________________________________")
print("↘ SIGNOS VITALES DEL PACIENTE ↙")
print("")
print(f"Temperatura Corporal| {tc_paciente} ")
print(f"Presion arterial|   {pa_sistolica}mmHg/{pa_diastolica}mmHg")
print(f"Latidos por minuto| {l_min}")
print("_______________________________________________________")
print("↘ CALCULOS DE SALUD DEL PACIENTE ↙")
print("")
print(f"Indice de masa corporal|    {c_salud[0]} Kg/m2")
print(f"Frecuencia cardiaca maxima| {c_salud[1]} ")
print(f"Presion arterial media|     {c_salud[2]} mmHg")
print("________________________________________________________")
print("↘ REGISTRO DE MEDICIONES CONTINUAS ↙")
print("")
print(f"Enfermedades          | {mediciones[0]}")
print(f"Alergias              | {mediciones[1]}")
print(f"Información adicional | {mediciones[2]}")
print("________________________________________________________")
