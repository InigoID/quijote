import sys
import random

def extraer_lineas_aleatorias(archivo_entrada, archivo_salida, porcentaje):
    with open(archivo_entrada, 'r', encoding='utf-8') as archivo_lectura, open(archivo_salida, 'w', encoding='utf-8') as archivo_escritura:
        for linea in archivo_lectura:
            if random.random() < porcentaje / 100:
                archivo_escritura.write(linea)

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    porcentaje = float(sys.argv[3])
    extraer_lineas_aleatorias(archivo_entrada, archivo_salida, porcentaje)
