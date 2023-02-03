# Calculadora de IMC
# Fórmula -> IMC = Peso / (altura)^2
# NOTA: La altura en metros
#
# Posibles resultados
# <19 -> Delgadez
# 20-25 -> Peso normal
# 26-30 -> Sobrepeso
# >30 -> Obesidad

# Función de calcular IMC, con la fórmula de arriba
def calcularIMC (peso, altura):
    imc = peso / (altura*altura)
    return imc

# Asignamos lo valores introducidos por teclado
peso = int(input('Introduce tu peso en kg: '))
altura = int(input('Introduce tu altura en cm: '))

# Lo pasamos a metros
altura = altura / 100

# Llamamos a la función y le pasamos los parámetros introducidos previamente para que haga el cálculo
imc = calcularIMC(peso,altura)

# Vemos el IMC obtenido para saber el estado físico
if(imc<19):
    estadoFisico = 'Delgadez'
if(imc>=20 and imc<=25):
    estadoFisico = 'Peso normal'
if(imc>=26 and imc<=30):
    estadoFisico = 'Sobrepeso'
if(imc>30):
    estadoFisico = 'Obesidad'

# Imprimimos por consola el resultado del IMC y el estado físico
print ('Tu IMC es: '+str(imc)+'\n'+'Tu estado físico es '+estadoFisico)