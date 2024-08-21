import preguntas as p
import random

def shuffle_alt(pregunta):
    """
    Baraja aleatoriamente las alternativas de una pregunta.

    Parámetros:
    pregunta (dict): Diccionario con una clave 'alternativas' que contiene una lista de alternativas.

    Retorno:
    list: Lista de alternativas barajada. Si está vacía, retorna la lista sin cambios.
    """
    alternativas = pregunta['alternativas']
    if not alternativas:
        pass
    else:
        random.shuffle(alternativas)
    return pregunta['alternativas']

if __name__ == '__main__':
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1']))


