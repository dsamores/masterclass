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
