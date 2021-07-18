def canciones_sin_repeticion(lista_de_canciones):
    canciones_sin_repetir = []
    for i in lista_de_canciones:
        if i not in canciones_sin_repetir:
            canciones_sin_repetir.append(i)
    return canciones_sin_repetir

def posiciones_con_cancion(posiciones, listaCanciones, cancion):
    listaConCancion = []
    for i in range (len(listaCanciones)):
        if (listaCanciones[i] == cancion and (i in posiciones)):
            listaConCancion.append(i)
    return listaConCancion

def solo_categoria_X(categoriaX, categoriaY):
    soloCategoriaX = []
    for i in categoriaX:
        if i not in categoriaY:
            soloCategoriaX.append(i)
    return soloCategoriaX

def cantidad_cambios(usuario1, usuario2):
    cambios_usuario1 = 0
    cambios_usuario2 = 0
    for i in usuario1:
        if i not in usuario2:
            cambios_usuario1 +=1
    for i in usuario2:
        if i not in usuario1:
            cambios_usuario2 +=1
    if (cambios_usuario1 >= cambios_usuario2):
        return cambios_usuario2
    else:
        return cambios_usuario1

