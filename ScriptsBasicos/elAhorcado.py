
haTerminado = False
intentos = 5

palabra = input('Introduce una palabra: ')
palabraArray = []
palabraDescubierta = []
# Metemos en el array la palabra caracter a caracter
for letra in palabra:
    palabraArray += letra
# Rellenamos la palabra descubierta con _ por caracter para simular la longitud de la palabra
for letra in palabra:
    palabraDescubierta += '_'

    print('\n\n\n\n\n\n\n\n')

# Mientras el juego no finalice (intentos=0 o acertar la palabra), se repite el bucle del juego
while(haTerminado==False):
    print(palabraDescubierta)

    tuvoLetra = False
    letraInput = input ('Introduce una letra: ')

    # Aquí recorremos un bucle con el tamaño igual a la longitud de la palabra (guardada en palabraArray)
    for i in range(palabraArray.__len__()):
        if(letraInput == palabraArray[i]): # Cuando la letra introducida coincide con alguna letra del array, esta se copia al array de palabraDescubierta
            palabraDescubierta[i] = letraInput
            tuvoLetra = True # Verificamos que al haber una letra, no se restará un intento

    # Si la letra introducida no coincide con ninguna letra del array, se te restará 1 intento
    if(tuvoLetra==False):
        print('La palabra no contiene letra ' + letraInput)
        intentos -= 1
        print('Te quedan ' + str(intentos) + ' intentos')

    # Condiciones de fin de juego
    # Si descubres la palabra, ganas y el juego termina
    # Si llegas a 0 intentos, pierdes y el juego termina
    if(palabraDescubierta==palabraArray):
        print('Has ganado!')
        print('La palabra era: '+palabra)
        haTerminado = True
    elif (intentos == 0):
        print('Has perdido')
        haTerminado = True
        print('La palabra era: '+palabra)