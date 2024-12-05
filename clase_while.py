#ciclo while

#while condicion:
    #bloque de codigo a repetir 

#ciclo FOR                                             ciclo WHILE
#requiere secuencia: si, como una lista o rango         No, depende de una condicion

#definir una variable que lleve el control del ciclo

# numero = 1 

# while numero <= 5:  #condicion para iterar n veces.....
#     print(numero)    
#     numero += 1

#CONTAREMOS HACIA ATRAS

# numero = 10
# while numero >= 1:
#     print(numero)
#     numero -= 1




#CREAR UN PROGRAMA QUE SUME NUMEROS INGREDOS POR EL USUARIO HASTA EL USUARIO INGRESE EL 0

# suma = 0

# numero = int(input("ingrese un numero o pulsa 0 para SALIR: "))

# while numero != 0:
#     suma += numero
#     numero = int(input("ingrese un numero o pulsa 0 para SALIR: "))
#     print(f"La suma total es: {suma}")



#el ciclo while se puede usar en condiciones dinamicas: 
#son aleatorias, y pueden cambiar con la ejecucion del codigo 

#simulacion basada en una condicion externa
#simular el crecimiento de una poblacion hasta que alcance un limite 

# poblacion = 1000
# limite = 5000
# tasa_crecimiento = 1.1 

# while poblacion < limite:
#     print(f"pobacion actual: {poblacion}")

#     poblacion = int(poblacion * tasa_crecimiento)

# print(f"poblacion final alcanzada: {poblacion}")



#lecturas de un sensor...
#simular la lectura de un sensor que me dira valores aleatorios hasta que alcance un valor objetivo


# import random 

# sensor = random.randint(0, 50)
# objetivo = 40
# contador = 1

# while sensor < objetivo:
#     print(f"en la lectura numero {contador}, el valor del sensor es: {sensor}")
#     sensor += random.randint(1, 10)
#     contador += 1
# print(f"la lectura final alcanzada fue: {sensor}")