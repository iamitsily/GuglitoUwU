import re
from collections import defaultdict
import os
import json

def buscar_palabra(palabra_buscada):
    archivo = os.path.join('ilysdjangoApp', 'raiz_ind_inv.txt')  # Reemplaza con la ruta a tu archivo
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
    resultados_json = {url: str(frecuencia) for url, frecuencia in frecuencia_urls.items()}
    return resultados_json
