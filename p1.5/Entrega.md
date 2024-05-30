# ENTREGA 

Flor Mayon - 22760045 

------------
### Flujo

Se importan los módulos "json" y "sys".
En el código se encuentran diez funciones:
- **cargar_tokens():** Se encarga de obtener los tokens y caracteres asociados del archivo.txt  para almacenarlos en un diccionario.
- **leer_json():** Lee el archivo.json y se asignan a una variable como cadena de caracteres.
- **procesar_caracteres():** Se pasan como parámetros en la función las variables obtenidas de las dos funciones anteriores. Se itera sobre cada caracter de la variable obtenida del archivo.json y si se encuentra en  el diccionario de tokens, se almacenan en una nueva lista el token y caracter encontrado. En caso de no encontrarse el caracter, imprime un mensaje de error y finaliza el programa.
- **confirmar_json():** Verifica que el archivo.json inicie y finalice con los caracteres "{ }".
- **confirmar_string():** Verifica que las comillas dobles sean par.
- **token_string():** Si los tokens asignados para ser un string se encuentran en el resultado del archivo.json, se le asigna un nuevo token general (555) para ese grupo de tokens.
- **token_numeric():** Procesa la lista de tokens y condiciona que si ciertos  tokens que representan un decimal o entero se encuentran, les asigna un nuevo token general a cada uno, decimal(777) y entero(666).
- **token_date():** Verifica que si los tokens que representan una fecha se encuentran  en el índice correspondiente y les asigna un nuevo token general (888).
- **main():** Contiene las funciones que procesan el archivo.json ,es decir, aquellas que permiten implementar el código como carga, lectura, confirmación y salida.
- **imprimir_tokens_json():** Imprime en consola los caracteres con el token asociado originalmente.


------------

### Alcance 
Hasta el momento lo que realiza este programa es lo siguiente:
- Abre un archivo.txt y lo carga a un diccionario.
- Abre un archivo.json y lo carga a una variable como cadena de caracteres.
- Almacena los caracteres con el token asociado que se encuentren en el archivo.json en una lista.
- Si un caracter del archivo.json no se encuentra en el catalgo_tokens.txt imprime un mensaje de error y finaliza el programa.
- Confirma que el archivo.json inicie y finalice con los caracteres propios de su sintaxis, en caso necesario imprime un mensaje de error y finaliza el programa.
- Confirma que se encuentren comillas dobles como par, es decir, cerradas, si no imprime un mensaje de error y finaliza el programa.
- Asigna un token general para un grupo de tokens:
    - String -> 555
    - Int ->666
    - Decimal ->777
    - Date -> 888
- Imprime los tokens y caracteres del archivo.json.
- Imprime los tokens y caracteres del archivo.json  y el token String.
- Imprime los tokens y caracteres del archivo.json y el token Int/Decimal.
- Imprime los tokens y caracteres del archivo.json y el token Date.

------------


### Proyección

Añadir más caracteres en el catalogo_tokens.txt.
Añadir más especificaciones para el procesamiento de un archivo.json por ejemplo:
1. Que se encuentren los corchetes “[ ]” correctos, tokenizar el arreglo y contenido de los corchetes se encuentre separado por “,” .
2. Que las comas “,” continúen después de cierto caracter.
3. Tokenizar valores null.
4. Tokenizar valores booleanos.
5. Confirmar que se encuentren correctamente los corchetes y llaves anidadas.

Por último, actualmente imprime los tokens agrupados de string/decimal/int/date por separado, me gustaría añadir una función que “combine” estos resultados para que se imprima en consola un solo resultado con los tokens que no se han agrupado más los que sí tiene un token general.