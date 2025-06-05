from collections import Counter

def analizar_texto(texto):
    palabras = texto.split()
    num_palabras = len(palabras)
    num_caracteres = len(texto)
    frecuencia_caracteres = Counter(texto.lower())
    palabras_comunes = Counter(palabras).most_common(5)
    
    return {
        "Número de palabras": num_palabras,
        "Número de caracteres": num_caracteres,
        "Frecuencia de caracteres": frecuencia_caracteres,
        "Palabras más comunes": palabras_comunes
    }


if __name__ == "__main__":
    print("Analizador de Texto")
    texto = input("Pega tu texto aquí:\n")
    resultados = analizar_texto(texto)
    
    print("\nResultados:")
    for clave, valor in resultados.items():
        print(f"{clave}: {valor}")