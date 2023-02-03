import random

eleccionArray = ['Piedra','Papel','Tijera']
finDeJuego = False
while(finDeJuego==False):
    eleccion = int(input('\nIntroduce (1) Piedra,(2) Papel o (3) Tijera o "0" para terminar el juego: '))
    if(eleccion == 0):
        finDeJuego=True
        break;
    eleccionString = eleccionArray[eleccion-1]
    eleccionIAString = eleccionArray[random.randrange(0,3)]
    resultado = ''

    if(eleccionString == 'Piedra' and eleccionIAString == 'Piedra' or eleccionString == 'Papel' and eleccionIAString == 'Papel'
        or eleccionString == 'Tijera' and eleccionIAString == 'Tijera'):
        resultado = 'Empate'
    elif (eleccionString == 'Piedra' and eleccionIAString == 'Papel' or eleccionString == 'Papel' and eleccionIAString == 'Tijera'
    or eleccionString == 'Tijera' and eleccionIAString == 'Piedra'):
        resultado = 'Pierdes'
    else:
        resultado = 'Ganas'

    print('Has elegido -> '+eleccionString)
    print('Tu rival ha elegido -> '+ eleccionIAString)
    print(resultado)