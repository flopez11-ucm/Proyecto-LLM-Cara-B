# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 09:34:56 2025

@author: Francisco Javier López Pacheco

"""

"""
def guardar_en_fichero(texto):
    # Abrimos el fichero en modo escritura ("w")
    # Si no existe, se crea; si existe, se sobrescribe
    with open("salida.txt", "w", encoding="utf-8") as f:
        f.write(texto)

# Ejemplo de uso
cadena = "Hola, esto es una prueba."
guardar_en_fichero(cadena)

def leer_fichero(nombre):
    with open(nombre, "r", encoding="utf-8") as f:
        contenido = f.read()
    return contenido

# Ejemplo de uso:
texto = leer_fichero("salida.txt")
print(texto)

"""

import json
from datetime import datetime

def guardar_resultado(
    nombre_fichero,
    pregunta_id,
    pregunta_texto,
    modelo,
    chunking,
    respuesta_llm,
    opcion_elegida,
    opcion_correcta,
    es_correcta,
    chunks_recuperados,
):
    entrada = {
        "timestamp": datetime.now().isoformat(),
        "pregunta_id": pregunta_id,
        "pregunta_texto": pregunta_texto,
        "modelo": modelo,                     # "BM25" o "Dense"
        "chunking": chunking,                 # tipo de chunking usado
        "respuesta_llm": respuesta_llm,       # string largo
        "opcion_elegida": opcion_elegida,     # "A", "B", ...
        "opcion_correcta": opcion_correcta,   # "B"
        "es_correcta": es_correcta,           # True/False
        "chunks_recuperados": chunks_recuperados,  # lista de IDs o textos
        "num_chunks": len(chunks_recuperados)
    }

    with open(nombre_fichero, "a", encoding="utf-8") as f:
        f.write(json.dumps(entrada, ensure_ascii=False) + "\n")


guardar_resultado(
    nombre_fichero="resultados.jsonl",
    pregunta_id=1,
    pregunta_texto="¿Qué afirma el artículo sobre X?",
    modelo="BM25",
    chunking="window_size_300_overlap_50",
    respuesta_llm="La respuesta es B porque... (explicación larga)",
    opcion_elegida="B",
    opcion_correcta="B",
    es_correcta=True,
    chunks_recuperados=[12, 13, 14]  # IDs de los chunks o strings directamente
)
