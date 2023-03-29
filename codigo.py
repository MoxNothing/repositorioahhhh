print('Bienvenido a la Aplicacion de Colecciones de Musica')

musica = []

def muestra():
    for musica in musica: 
        print('autor: ', musica['autor'])
        print('album: ', musica['album'])
        print('cantante: ', musica['cantante'])
        print('nombre: ', musica['nombre'])
        print('ano: '), musica['ano']

def a_musica():
        
    musica={}
    
    musica['autor'] = input('digita el autor: ')
    musica['album'] = input('digita el album: ')
    musica['cantante'] = input('digita el cantante: ')
    musica['nombre'] = input('digita el nombre: ')
    musica['ano'] = input('digita el ano: ')

    musica.append(musica)
    print('la cancion a sido agregada correctamente')
    

def actualiza():
    menu = int(input('ingresa la actualizacion de la musica'))
    if menu >= 0 and musica < len(musica):
        musica = musica[menu]
        musica['autor'] = input('ingresa autor :')
        musica['album'] = input('ingresa album :')
        musica['cantante'] = input('ingresa cantante :')
        musica['nombre'] = input('ingresa nombre :')
        musica['ano'] = input('ingresa ano :')
        print('la cancion ha sido actualizada')
    else:
        print('menu invalidado')

def eliminar():
    menu = int(input('ingresa la cancion a eliminar : '))
    if menu >= 0 and menu < len(musica):
        del musica[menu]
        print('elimnar musica')
    else:
        print('en el menu la cancion no existe')

def limpia():
    musica.clear()
    print('limpieza de canciones realizada')

while True:
    print("1. nueva musica")
    print("2. agregar musica")
    print("3. actualizar musica")
    print("4. eliminar musica")
    print("5. limpiar musicas")
    print("6. salir")

    eleccion = int(input("Entrar eleccion:"))
    if eleccion == 1:
        muestra()
    elif eleccion == 2:
        a_musica()
    elif eleccion == 3:
        actualiza()
    elif eleccion == 4:
        eliminar()
    elif eleccion == 5:
        limpia()
    elif eleccion == 6:
        break
    else:
        print("Eleccion invalida")

        
