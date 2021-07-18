def run():

    vehiculos = input('Ingrese la letras de los vehiculos registrados: ')
    vehiculos = vehiculos.strip()
    vehiculos = vehiculos.upper()
    vehiculos = vehiculos.replace(' ', '')

    letra_anterior = ''
    lista_letras = []
    numero_letras = []


    for letras in vehiculos:
        if len(lista_letras) == 0 or letras != lista_letras[-1]:
            lista_letras.append(letras)
            numero_letras.append(1)

        
        if letra_anterior != '' and letra_anterior ==  letras:
            numero_letras[-1] += 1

        letra_anterior = letras

    print(*lista_letras)
    print(*numero_letras)      
            

if __name__ ==  '__main__':
    run()
