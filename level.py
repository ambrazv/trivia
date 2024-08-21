def choose_level(n_pregunta, p_level):
    """Permite escoger el nivel de dificultad de la pregunta a realizar.
    Parámetros
    ----------
    n_pregunta: int
        El número de la pregunta actual.
    p_level: int
        La cantidad de preguntas por nivel(puede ser 2 o 3).
    Returns
    -------
    level: str
        El nivel de dificultad seleccionado: 'básicas', 'intermedias' o 'avanzadas'.
    """
    if 1 <= n_pregunta <= p_level:
        level = "basicas"
    elif p_level <= n_pregunta <= 2 * p_level:
        level = "intermedias"
    else:
        level = "avanzadas"

    return level


if __name__ == "__main__":
    # verificar resultados
    print(choose_level(2, 2))  # básicas
    print(choose_level(3, 2))  # intermedias
    print(choose_level(7, 2))  # avanzadas
    print(choose_level(4, 3))  # intermedias
