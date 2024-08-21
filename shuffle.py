import random
import preguntas as p

def shuffle_alt(pregunta):
    """
    Mezcla aleatoriamente las alternativas de una pregunta.

    Parámetros
    ----------
    alternativas : list
        Lista de alternativas, donde cada alternativa es a su vez una lista
        con la forma [texto_de_la_alternativa, es_correcta].

    Returns
    -------
    list
        Lista de alternativas mezclada aleatoriamente.
    """
    # mezclar alternativas
    #######################################################################
    random.shuffle(pregunta)
    #######################################################################
    
    return pregunta

if __name__ == '__main__':
    # Si se ejecuta el programa varias veces, las alternativas debieran aparecer en distinto orden
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1']['alternativas']))
    # a modo de ejemplo, el resultado podría ser:
    # [['1820', 0], ['1810', 1], ['1800', 0], ['1830', 0]]




