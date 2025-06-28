print("Hola! Soy un robot analizador de texto. Como te llamas?")

nombre = input()

print(f"Mucho gusto {nombre}!")

print("Ingresa una frase para analizar:")

frase = input()

print(f"Esta frase tiene {len(frase)} caracteres")

vocales = 0

for i in frase.lower():
    if i in "aeiou":
        vocales += 1

print(f"Tiene {vocales} vocales")

print(f"Comienza con {frase[0]}")
print(f"Termina con {frase[-1]}")

print("Análisis de palabras:")

palabras = frase.split()

print(f"La frase tiene {len(palabras)} palabras")

# primera palabra y ultima palabra
print(f"La primera palabra es {palabras[0]}")
print(f"La ultima palabra es {palabras[-1]}")

# imprimir la cantidad de consonantes en cada una de las palabras
for palabra in palabras:
    consonantes = 0
    for i in palabra:
        if i not in "aeiou":
            consonantes += 1
    print(f"La palabra {palabra} tiene {consonantes} consonantes")
