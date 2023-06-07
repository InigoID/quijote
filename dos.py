import sys
import string

def contar_palabras(archivo_entrada, archivo_salida):
    conteo_palabras = {}

    with open(archivo_entrada, 'r', encoding='utf-8') as archivo_lectura:
        for linea in archivo_lectura:
            linea = linea.translate(str.maketrans("", "", string.punctuation))
            palabras = linea.strip().split()
            for palabra in palabras:
                palabra = palabra.lower()
                conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

    with open(archivo_salida, 'w', encoding='utf-8') as archivo_escritura:
        for palabra, conteo in conteo_palabras.items():
            archivo_escritura.write(f'{palabra}: {conteo}\n')

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]

    contar_palabras(archivo_entrada, archivo_salida)
