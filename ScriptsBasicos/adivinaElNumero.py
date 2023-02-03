# Adivina el número
# Juego donde se generará un número aleatorio entre un rango mínimo y máximo y el jugador irá probando
# hasta 5 intentos, y el juego le dirá si el número es mayor o menor al introducido por teclado
import random

finDeJuego = False
intentos = 5
mayorMenor = ""
numeroAleatorio = random.randrange(1, 50) # Generamos un número aleatorio entre 1 y 50


while (finDeJuego==False):
    if(intentos==0):
        print("Fin de juego! El número era: "+str(numeroAleatorio))
        finDeJuego=True

    if(intentos > 0):
        numeroIntroducido = int(input("Introduce un número (1-50): ")) # Introducimos por teclado el número

        if(numeroIntroducido == numeroAleatorio):
            print("Has ganado!. El número era: "+str(numeroAleatorio))
            finDeJuego = True
        elif (numeroIntroducido < 1 or numeroIntroducido > 50):
            print("Fuera de rango")
        elif (numeroIntroducido < numeroAleatorio):
            intentos=intentos-1
            mayorMenor = "MENOR"
        elif (numeroIntroducido > numeroAleatorio):
            intentos=intentos-1
            mayorMenor = "MAYOR"

        if(intentos > 0 and finDeJuego == False):
            print("El número introducido es "+mayorMenor+" que el número a adivinar. Te quedan "+str(intentos)+ " intentos")
        elif(intentos==0):
            print("Te quedaste sin intentos.")


