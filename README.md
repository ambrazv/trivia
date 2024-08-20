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
    git clone https://github.com/tu_usuario/trivia_app.git
    ```

2. **Accede al directorio del proyecto:**

    ```bash
    cd trivia_app
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
- `shuffle.py`: Contiene la función `shuff
