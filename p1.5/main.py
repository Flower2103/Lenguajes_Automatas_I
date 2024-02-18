import json

# Diccionario para almacenar los tokens del archivo .txt
tokens = {}

# Lista para almacenar el resultado de tokens y caracteres encontrados en el archivo .json
resultado_tokens = []

# Cargar tokens desde el archivo
with open('p1.5/catalogo_tokens.txt', 'r') as archivo_tokens:
    for linea in archivo_tokens:
        clave, valor = linea.strip().split(':')
        tokens[clave] = valor


# Abrir archivo JSON, leer y asignarlo a la variable data
with open('p1.5/nombre.json', 'r') as myfile:
    data = myfile.read()


"""
# Recorre los caracteres de la variable "data" y almacena los tokens y caracteres
  correspondientes en  <list> "resultado_tokens" si estos se encuentra en el <dic> "tokens", 
  los que no se encuentran en el diccionrio se condicionaron.
"""
for caracter in data:
    if caracter in tokens:
        resultado_tokens.append((tokens[caracter], caracter))
    elif caracter == ' ':
        resultado_tokens.append(('32', '[ESPACIO]'))  
    elif caracter == '\n':
        resultado_tokens.append(('10', '[ENTER]'))    
    elif caracter == ':':
        resultado_tokens.append(('58', ':'))         

# Imprime los resultados de la lista
for token, caracter in resultado_tokens:
    print(f"{token} := {caracter}")
