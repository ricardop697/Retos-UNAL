print("***programa para calcular la velocidad maxima de los aviones***")
import math

def categoria(velocidad):
  if 0 <= velocidad <= 20:
    return "uno"
  elif 21 <= velocidad <= 30:
    return "dos"
  elif 31 <= velocidad <= 50:
    return "tres"
  else:
    return "cuatro"

velocidad = input("ingrese la velocidad del avion: \n")
  
avion_a = int(velocidad)
avion_b = (avion_a * 2) + 4 
avion_c = math.floor((avion_a + avion_b) // 5)

cat = categoria(avion_c)

print(f"{avion_a} {avion_b} {avion_c} {cat}")

  
  
    
