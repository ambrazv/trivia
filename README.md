# Trivia App - Proyecto de Fundamentos de Programación en Python

## Descripción del Proyecto

Este proyecto es una aplicación de trivia interactiva desarrollada en Python. La aplicación permite a los usuarios jugar un quiz con preguntas de diferentes niveles de dificultad: Básico, Intermedio y Avanzado. Los jugadores pueden definir el número de preguntas por nivel y ganan el juego al responder correctamente todas las preguntas. Las preguntas y alternativas se presentan en orden aleatorio para evitar patrones.

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instalado:

- **Sistema Operativo:** Windows, Linux, macOS
- **Lenguaje de programación:** Python 3.12 o superior

## Instalación del Proyecto

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/trivia.git
   ```

2. **Accede al directorio del proyecto:**

   ```bash
   cd trivia
   ```

## Instrucciones para Ejecutar el Proyecto

1. **Ejecuta el script principal:**

   ```bash
   python main.py
   ```

2. **Sigue las instrucciones en el menú interactivo para jugar a la trivia.**

## Estructura de Archivos

- `main.py`: Archivo principal que ejecuta la aplicación. Maneja la lógica del juego, la selección de preguntas y la validación de respuestas.
- `preguntas.py`: Contiene diccionarios con preguntas y alternativas organizadas por niveles de dificultad (básicas, intermedias, avanzadas).
- `question.py`: Define la función `choose_q()` para seleccionar una pregunta aleatoria de acuerdo a la dificultad.
- `shuffle.py`: Contiene la función `shuffle_alt()` que mezcla las alternativas de una pregunta.
- `print_preguntas.py`: Incluye la función `print_pregunta()` para imprimir el enunciado y las alternativas de una pregunta en un formato amigable.
- `level.py`: Define la función `choose_level()` para determinar el nivel de dificultad de las preguntas basado en el número de preguntas por nivel.
- `validador.py`: Contiene la función `validate()` para validar que una opción ingresada por el usuario esté dentro de un conjunto de opciones.
- `verify.py`: Incluye la función `verificar()` para verificar si la respuesta del usuario es correcta.

## Requerimientos del Proyecto

1. **Manipulación de Variables y Estructuras de Datos:** Crea y utiliza variables y estructuras de datos adecuadas.
2. **Definición de Funciones:** Crea funciones con diferentes tipos de variables y parámetros siguiendo buenas prácticas.
3. **Modularización del Código:** Estructura el código en archivos Python modulares.
4. **Validación y Pruebas:** Valida y prueba adecuadamente las funciones y el programa para asegurar el correcto funcionamiento.

## Autores

- Ambar Zambrano
- Karen Limari
- Arlenis Gonzalez

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo `LICENSE.md` para más detalles.

---

**Notas:**

- Reemplaza `https://github.com/tu_usuario/trivia.git` con la URL correcta de tu repositorio en GitHub.
- Asegúrate de tener un archivo `LICENSE.md` en el repositorio si mencionas la Licencia MIT.
- Guarda el contenido anterior en un archivo llamado `README.md` en el directorio raíz de tu proyecto para proporcionar documentación clara sobre el mismo.
