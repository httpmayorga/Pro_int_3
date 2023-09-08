import readchar
print("Inserte su nombre por favor")
nombre=input()
print("Bienvenido "+ nombre + " al laberinto de la anaconda")

while True:
   key = readchar.readkey()
   print(f"Tecla presionada: {key}")
   if key == readchar.key.UP:
         print("Se presionó la tecla de flecha hacia arriba. Saliendo del bucle.")
         break
    
#Para esta sección del proyecto integrador necesitaremos aprender a manipular la terminal:

#Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, borrar la terminal y e imprimir el nuevo número hasta el número 50.

#La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función.

#Para borrar la terminal antes de imprimir nuevo contenido usar la instrucción: os.system('cls' if os.name=='nt' else 'clear'), para esto se debe importar la librería os