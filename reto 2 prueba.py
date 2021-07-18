def asignar_punto(venta,videojuegos_vendidos):
    return 1 if (venta in videojuegos_vendidos) else 0

def mas_vendido(videojuego_deportes,videojuego_estrategia):
    if videojuego_deportes > videojuego_estrategia:
        return "D"
    elif videojuego_deportes < videojuego_estrategia:
        return "E"
    else:
        return "Z"

venta_deportes = input("Ingrese lista de videojuegos de deportes: ")
venta_estrategia = input("Ingrese lista de videojuegos de estrategia: ")
otro_juego = input("Ingrese lista de videojuegos vendidos: ")
videojuego_deportes = 0
videojuego_estrategia = 0
resultado_final = ""
for venta in otro_juego:
    videojuego_deportes += asignar_punto(venta,venta_deportes)
    videojuego_estrategia += asignar_punto(venta,venta_estrategia)
    resultado_final += mas_vendido(videojuego_deportes,videojuego_estrategia)
    
print(f"El resultado de analisis de ventas: {resultado_final}")
