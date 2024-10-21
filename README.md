# Proyecto de Análisis Léxico - Lenguaje AC

Este proyecto implementa un analizador léxico para el lenguaje de programación **AC** usando `flex` y `gcc`. El analizador reconoce declaraciones de variables, asignaciones, expresiones aritméticas, impresión de variables, y comentarios en el código. Además, identifica símbolos como operadores aritméticos y paréntesis.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes programas en tu entorno de desarrollo (Linux):

- **flex**: Para generar el código en C desde el archivo de análisis léxico (`lex_analyzer.l`).
- **gcc**: Para compilar el código generado y crear el ejecutable.
- **make**: Para automatizar el proceso de compilación.

- Instrucciones de Uso
1. Compilación del Analizador Léxico
Para compilar el analizador léxico, simplemente ejecuta el siguiente comando en el directorio donde se encuentra el archivo Makefile:
**make**

Esto ejecutará los siguientes pasos automáticamente:

flex lex_analyzer.l: Generará el archivo lex.yy.c.
gcc -o lex_analyzer lex.yy.c -lfl: Compilará el archivo generado y creará un ejecutable llamado lex_analyzer.

2. Ejecución del Analizador Léxico
Una vez que el analizador ha sido compilado, puedes ejecutarlo sobre un archivo de código fuente en el lenguaje AC. Por ejemplo, si tienes un archivo example.ac, usa el siguiente comando:
**./lex_analyzer example.ac**

