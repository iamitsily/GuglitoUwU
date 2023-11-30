import re
from collections import defaultdict
import json

def buscar_palabra(archivo, palabra_buscada):
    # Utilizamos un defaultdict para contar la frecuencia de cada URL
    frecuencia_urls = defaultdict(int)

    # Leemos el archivo línea por línea
    with open(archivo, 'r', encoding='utf-8') as file:
        # Leemos el contenido completo del archivo
        contenido = file.read()

        # Utilizamos expresiones regulares para buscar la palabra clave y sus URLs y frecuencias
        resultados = re.findall(rf'\[Palabra:\s{palabra_buscada}:\s\((https:\/\/.*?)\,\sFrecuencia:\s(\d+)\)\]', contenido)

        # Iteramos sobre las coincidencias y actualizamos el contador de frecuencia
        for url, frecuencia in resultados:
            frecuencia_urls[url] += int(frecuencia)

    # Devolvemos el resultado como un diccionario
    resultados_json = json.dumps(dict(frecuencia_urls), indent=2)
    return resultados_json

if __name__ == "__main__":
    palabra_a_buscar = input("Palabra a buscar: ")
    archivo_a_analizar = 'index2.txt'  # Reemplaza con la ruta a tu archivo

    resultados = buscar_palabra(archivo_a_analizar, palabra_a_buscar)

    if resultados:
        print(f"Resultados para '{palabra_a_buscar}':")
        print(resultados)
    else:
        print(f"No se encontraron resultados para '{palabra_a_buscar}'.")
