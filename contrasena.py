import random
import string

def generar_contraseña(longitud=12, mayusculas=True, numeros=True, simbolos=True):
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation
    
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Ejemplo de uso
if __name__ == "__main__":
    print("Generador de Contraseñas Seguras")
    longitud = int(input("Longitud de la contraseña: "))
    mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
    numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'
    
    contraseña = generar_contraseña(longitud, mayusculas, numeros, simbolos)
    print(f"\nTu contraseña generada es: {contraseña}")