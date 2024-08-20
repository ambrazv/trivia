import preguntas as p  
import random
from shuffle import shuffle_alt  # Verificar este módulo para mezclar alternativas 

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1, 2, 3],
            'intermedias': [1, 2, 3],
            'avanzadas': [1, 2, 3]}
###############################################

def choose_q(dificultad):
    global opciones  # Usar opciones desde ambiente global

    # Escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]  # Acceder al conjunto de preguntas según la dificultad
    
    if not opciones[dificultad]:
        raise ValueError("No hay más preguntas disponibles para esta dificultad.")
    
    # Escoger una pregunta aleatoria
    n_elegido = random.choice(opciones[dificultad])
    opciones[dificultad].remove(n_elegido)  # Eliminarla del ambiente global para no escogerla de nuevo
    
    # Convertir el número elegido en la clave del diccionario
    clave_pregunta = f'pregunta_{n_elegido}'
    
    # Obtener la pregunta y alternativas
    pregunta = preguntas[clave_pregunta]
    enunciado = pregunta['enunciado'][0]  # Obtener el enunciado de la pregunta
    alternativas = pregunta['alternativas']  # Obtener las alternativas
    
    # Mezclar alternativas usando el método shuffle_alt del archivo shuffle.py
    alternativas_mezcladas = shuffle_alt(alternativas)
    
    return enunciado, alternativas_mezcladas

if __name__ == '__main__':
    # Si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
