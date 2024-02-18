import json

# Diccionario para almacenar los tokens
tokens = {}

# Cargar tokens desde el archivo
with open('p1.5/catalogo_tokens.txt', 'r') as archivo_tokens:
    for linea in archivo_tokens:
        clave, valor = linea.strip().split(':')
        tokens[clave] = valor

# Lista para almacenar los resultados
resultado_tokens = []

# Abrir archivo JSON, leer y asignarlo a la variable data
with open('p1.5/nombre.json', 'r') as myfile:
    data = myfile.read()

# Recorrer los caracteres del archivo JSON y generar los tokens correspondientes
for caracter in data:
    if caracter in tokens:
        resultado_tokens.append((tokens[caracter], caracter))
    elif caracter == ' ':
        resultado_tokens.append(('32', '[ESPACIO]'))  
    elif caracter == '\n':
        resultado_tokens.append(('10', '[ENTER]'))    
    elif caracter == ':':
        resultado_tokens.append(('58', ':'))         

# Imprimir los resultados
for token, caracter in resultado_tokens:
    if token == '32':
        print(f"{token} := {caracter}")
    elif token == '10':
        print(f"{token} := {caracter}")
    elif token == '58':
        print(f"{token} := {caracter}")
    else:
        print(f"{token} := {caracter}")