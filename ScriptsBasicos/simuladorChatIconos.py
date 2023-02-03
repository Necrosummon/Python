# Simulador de chat con iconos
# Hacer un "chat" donde al escribir determinados caracteres los reemplaze por emojis
# Ejemplo -> :) pasaría a ser 🙂
# La lista está aquí -> https://es.piliapp.com/emoji/list/
# Nos pedirá un nickname para saber quien escribe (hablaremos solos pues es offline)
# Para salir del chat, no escribiremos nada
#

# Registramos el nickname
nickname = input('Introduce tu nickname: ')

# Controlamos si queremos finalizar el chat, por defecto no.
finDeChat = False

# Entramos en un bucle, donde si queremos seguir chateando, deberemos escribir algo, para repetir el input
# de lo contrario, el chat habrá finalizado.
while finDeChat==False:
    #Creamos una variable que recojerá lo escrito por teclado
    textoChat = input('> ')

    # Si no escribimos nada, es que no queremos seguir chateando
    if textoChat == '':
        finDeChat = True
    else:
        # Vamos a registrar los posibles emojis
        textoChat = textoChat.replace(':)','🙂')

        # Envíamos el texto a la consola
        print('['+nickname+']: '+textoChat)