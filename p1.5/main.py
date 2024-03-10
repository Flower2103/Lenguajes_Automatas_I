import json

tokens = {} # Diccionario para almacenar los tokens del archivo .txt

# Cargar tokens desde el archivo.txt
def catalogo_tokens():
    with open('p1.5/catalogo_tokens.txt', 'r') as archivo_tokens:
        for linea in archivo_tokens:
            clave, valor = linea.strip().split(':')
            tokens[clave] = valor


# Abrir archivo JSON, leer y asignarlo a la variable data
def leer_json():
    with open('p1.5/nombre.json', 'r') as myfile:
        data = myfile.read()
    return data


"""
# Recorre los caracteres de la variable "data" y almacena los tokens y caracteres
  correspondientes en  <list> "resultado_tokens" si estos se encuentra en el <dic> "tokens", 
  los que no se encuentran en el diccionrio se condicionaron.
"""
def procesar_caracteres(data, tokens):
    resultado_tokens = [] # Lista para almacenar el resultado
    for caracter in data:
        if caracter in tokens:
            resultado_tokens.append((tokens[caracter], caracter))
        elif caracter == ' ':
            resultado_tokens.append(('32', '[ESPACIO]'))  
        elif caracter == '\n':
            resultado_tokens.append(('10', '[ENTER]'))    
        elif caracter == ':':
            resultado_tokens.append(('58', ':')) 
    return resultado_tokens        


def main():
    catalogo_tokens()
    data = leer_json()
    resultado = procesar_caracteres(data , tokens)
    # Imprime los resultados de la lista
    for token, caracter in resultado:
        print(f"{token} := {caracter}")


if __name__=="__main__":
    main()