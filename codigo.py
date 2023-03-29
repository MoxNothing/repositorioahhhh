print('Bienvenido a la Aplicacion de Colecciones de Musica')

musica = []

def muestra():
    for musica in musica: 
        print('autor: ', musica['autor'])
        print('album: ', musica['album'])
        print('cantante: ', musica['cantante'])
        print('nombre: ', musica['nombre'])
        print('ano: '), musica['ano'])

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
    if menu >= 0 and index < len(musica):
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


        
