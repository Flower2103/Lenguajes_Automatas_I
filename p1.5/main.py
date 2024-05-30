# Flor Jazmin Mayon Cisneros
# Lenguajes y Automatas

import json
import sys

tokens = {} # Diccionario para almacenar los tokens del archivo .txt
# Cargar tokens desde el archivo.txt
def cargar_tokens():
    with open('p1.5/catalogo_tokens.txt', 'r') as archivo_tokens:
        for linea in archivo_tokens:
            clave, valor = linea.strip().split(':')
            tokens[clave] = int(valor)
    return tokens

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
            resultado_tokens.append((32, '[ESPACIO]'))  
        elif caracter == '\n':
            resultado_tokens.append((10, '[ENTER]'))    
        elif caracter == ':':
            resultado_tokens.append((58, ':')) 
        else:
            print(f"Error: el caracter '{caracter}' no tiene un token asociado.")
            sys.exit(1) 
    return resultado_tokens   
     

def confirmar_json(array):
    if array[0][0] == 123 and array[-1][0] == 125:
        return True
    else:
        print("[!] Error: El archivo no cumple con la estructura de inicio y/o fin de un JSON.")
        sys.exit(1)


def confirmar_string(array):
    flag = False  
    for token, _ in array:
        if token == 34:  # Verificar si es un token de comilla doble
            flag = not flag  # Cambiar el estado de la bandera
    if flag: # Si la bandera es True hay comillas sin cerrar
        print("ERROR: Las comillas no se cerraron correctamente")
        sys.exit(1)


def token_string(array):
    tokens= []
    grupo_string = False

    for token, _ in array:  
        if (token >= 65 and token <= 90) or (token >= 97 and token <= 122):
            if not grupo_string:
                tokens.append(555)
                grupo_string = True
        else:
            grupo_string = False
            tokens.append(token)
    return tokens


def token_numeric(array):
    tokens = []
    grupo_decimal = False
    grupo_int = False

    for token, _ in array:
        if ( token >= 48 and token <= 57):
            if not grupo_int and not grupo_decimal:
                tokens.append(666) # entero
                grupo_int = True
        elif (token == 46):
            if grupo_int:
                tokens.pop()
                tokens.append(777) # decimal
                grupo_decimal = True
        else: 
            grupo_int = False
            grupo_decimal = False
            tokens.append(token)
    return tokens


def token_date(array):
    tokens = [] 
    buffer = [] # Almacenar digitos de la fecha

    for token, _ in array:
        if ( token >= 47 and token <= 57):  
            buffer.append(token)
        else:
            if len(buffer) == 10 and buffer[4] == 47 and buffer[7] == 47: # 10 datos de la fecha e índices para diagonal
                    tokens.append(888)  # Token para fecha
                    buffer = []
            else:
                tokens.extend(buffer)
                buffer = []
            tokens.append(token)
    return tokens


def main():
    tokens = cargar_tokens()
    data = leer_json()

    resultado = procesar_caracteres(data , tokens)

    tokens_string = token_string(resultado)
    tokens_numeric = token_numeric(resultado)
    tokens_date = token_date(resultado)

    confirmar_json(resultado)
    confirmar_string(resultado)
    imprimir_tokens_json(resultado)

    print("\nSTRING: " + str(tokens_string))
    print("\nINT/DECIMAL: " + str(tokens_numeric))
    print("\nDate: " + str(tokens_date))

def imprimir_tokens_json(resultado):
    for token, caracter in resultado:
        print(f"{token} := {caracter}")

if __name__=="__main__":
    main()
