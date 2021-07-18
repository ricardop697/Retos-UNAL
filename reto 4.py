import json
def run ():
    
    entrada_json = input()
    entrada_python = json.loads(entrada_json)
    entrada2 = input().split(" ")

    inventario = input('Ingrese los productos solicitados: ')
    inventario = inventario.strip()
    inventario = inventario.upper()
    inventario = inventario.replace(' ', '')

suma_productos = 0
productos_encontrados = []
inventario_local = []

for productos in inventario:
        if len(productos_encontrados) == 0 or productos != productos_encontrados[-1]:
            productos_encontrados.append(productos)
            inventario_local.append(1)

        
        if suma_productos != '' and suma_productos ==  productos:
            inventario_local[-1] += 1

        suma_productos = productos

        print(*productos_encontrados)
        print(*inventario_local)      
            

if __name__ ==  '__main__':
    run()
