def choose_level(n_pregunta, p_level):
    """Permite escoger el nivle de dificultad de la pregunta a relaizar.
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

    # Construir lógica para escoger el nivel
    ##################################################
    pass

    ##################################################

    return level


if __name__ == "__main__":
    # verificar resultados
    print(choose_level(2, 2))  # básicas
    print(choose_level(3, 2))  # intermedias
    print(choose_level(7, 2))  # avanzadas
    print(choose_level(4, 3))  # intermedias
