# Flor Jazmin Mayon Cisneros
# Lenguajes y Automatas

import json

tokens = {} # Diccionario para almacenar los tokens del archivo .txt
# Cargar tokens desde el archivo.txt
def cargar_tokens():
    with open('lenguajes_A1/catalogo_tokens.txt', 'r') as archivo_tokens:
        for linea in archivo_tokens:
            clave, valor = linea.strip().split(':')
            tokens[clave] = int(valor)
    return tokens

# Abrir archivo JSON, leer y asignarlo a la variable data
def leer_json():
    with open('lenguajes_A1/nombre.json', 'r') as myfile:
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
            resultado_tokens.append((32, '[ESPACIO]'))  
        elif caracter == '\n':
            resultado_tokens.append((10, '[ENTER]'))    
        elif caracter == ':':
            resultado_tokens.append((58, ':')) 
    return resultado_tokens   
     

def confirmar_json(array):
    if array[0][0] == 123 and array[-1][0] == 125:
        return True
    else:
        print("[!] Error: El archivo no cumple con la estructura de inicio y/o fin de un JSON.")
        exit()


def confirmar_string(array):
    flag = False  
    for token, _ in array:
        if token == 34:  # Verificar si es un token de comilla doble
            flag = not flag  # Cambiar el estado de la bandera
    if flag:
        print("ERROR: Las comillas no se cerraron correctamente")
        exit()


def token_string(array):
    tokens= []
    agrupados = False

    for token, _ in array:  
        if (token >= 65 and token <= 90) or (token >= 97 and token <= 122):
            if not agrupados:
                tokens.append(555)
                agrupados = True
        else:
            agrupados = False
            tokens.append(token)
    return tokens


def main():
    tokens = cargar_tokens()
    data = leer_json()
    resultado = procesar_caracteres(data , tokens)

    confirmar_json(resultado)
    token_string(resultado)
    confirmar_string(resultado)
    
    imprimir_tokens_json(resultado)
    print(token_string(resultado))

def imprimir_tokens_json(resultado):
    for token, caracter in resultado:
        print(f"{token} := {caracter}")

if __name__=="__main__":
    main()