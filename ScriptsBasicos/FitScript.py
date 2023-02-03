# Script para calcular:
# 1 -> IMC
# 2 -> Gasto calórico diario

finDePrograma = False
sexo = ''

# Formula de calculo de IMC
def calcularIMC (peso, altura):
    imc = peso / (altura*altura)
    return imc

# Formula de calculo de gasto calórico diario
def calcularGastoCaloricoDiario(sexo,altura,peso,edad):

    if sexo == 'H':
        gastoCalorico = (66 + (13.7 * peso) + (5 * altura) - (6.5 * edad))
    else:
        gastoCalorico = (655 + (9.6 * peso) + (1.8 * altura) - (4.7 * edad))

    return gastoCalorico

# Bucle "main" del programa
while(finDePrograma==False):
    # Menú de consola
    print('\nElige una opción:')
    print('1. Calcular IMC')
    print('2. Calcular gasto calórico diario')
    print('3. Salir del programa')
    opcion = int(input('Introduce la opción: '))

    if opcion == 1:
        altura = int(input('Introduce tu estatura en cms: '))
        peso = int(input('Introduce tu peso en kgs: '))
        altura = altura / 100 # Pasar a metros
        imc = calcularIMC(peso,altura)
        print('Tu IMC es '+str(imc))
        if(imc<19):
            print('Tu estado físico es: Delgadez')
        elif(imc>=20 and imc<=25):
            print('Tu estado físico es: Peso normal')
        elif(imc>=26 and imc<=30):
            print('Tu estado físico es: Sobrepeso')
        else:
            print('Tu estado físico es: Obesidad')

    if opcion == 2:
        while sexo != 'H' and sexo != 'M':
            sexo = input('Introduce tu sexo:\n\t H-> Hombre\n\t M-> Mujer \n\t  Elección:')

        edad = int(input('Introduce tu edad: '))
        altura = int(input('Introduce tu estatura en cms: '))
        peso = int(input('Introduce tu peso en kgs: '))
        gastoCalorico = calcularGastoCaloricoDiario(sexo,altura,peso,edad)
        print('Tu gasto calórico diario  ' + str(gastoCalorico))

    if opcion == 3:
        finDePrograma=True
