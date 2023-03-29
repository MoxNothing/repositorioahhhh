musica = []

def muestra():
    for music in musica:
        print('autor:', music['autor'])
        print('album:', music['album'])
        print('cantante:', music['cantante'])
        print('nombre :', music['nombre '])
        print('ano:', music['ano'])
        

def agrega():
    music = {}
    music['autor'] = input('ingresa autor: ')
    music['album'] = input('ingresa album: ')
    music['cantante'] = input('ingresa cantante : ')
    music['nombre '] = input('ingresa nombre : ')
    music['ano'] = input('ingresa ano : ')
    musica.append(music)
    print('la cancion a sido agregada correctamente')
    

def actualiza():
    menu = int(input('ingresa la actualizacion de la musica : '))
    if menu >= 0 and menu < len(musica):
        music = musica[menu]
        music['autor'] = input('ingresa autor : ')
        music['album'] = input('ingresa album : ')
        music['cantante'] = input('ingresa cantante : ')
        music['nombre'] = input('ingresa nombre : ')
        music['ano'] = input('ingresa ano : ')
        print('la cancion ha sido actualizada')
        
    else:
        print('menu invalido')

def elimina():
    menu = int(input('ingresa la cancion a eliminar :'))
    if menu >= 0 and menu < len(musica):
        del musica[menu]
        print('eliminar musica')
        
    else:
        print('en el menu de canciones no existe')

def limpia():
    musica.clear()
    print('limpieza de canciones realizada')
    

while True:
    print('1. ver musica')
    print('2. agregar musica')
    print('3. actualizar musica')
    print('4. eliminar musica')
    print('5. limpiar musica')
    print('6. salir')
    eleccion = int(input('ingresa eleccion: '))
    if eleccion == 1:
        muestra()
    elif eleccion == 2:
        agrega()
    elif eleccion == 3:
        actualiza()
    elif eleccion == 4:
        elimina()
    elif eleccion == 5:
        limpia()
    elif eleccion == 6:
        break
    else:
        print('Eleccion invalida')