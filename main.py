import os
import readchar

def borrar_y_mostrar_numero(i):
    os.system('cls' if os.name == 'nt' else 'clear')
    if i==50:
         print("Se conto 50 veces, finalizacion del prorgama")
   
    else:
         print(f"Número: {i}")
    

i= 0

while i <= 50:
    # Espera a que se presione la tecla "n"
    
    key = readchar.readkey()
    
    if key == 'n':
        borrar_y_mostrar_numero(i)
        i += 1


#Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, borrar la terminal y e imprimir el nuevo número hasta el número 50.

#La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función.

#Para borrar la terminal antes de imprimir nuevo contenido usar la instrucción: os.system('cls' if os.name=='nt' else 'clear'), para esto se debe importar la librería os