def choose_level(n_pregunta, p_level):
    """Permite escoger el nivel de dificultad de la pregunta a realizar.
    
    Parámetros
    ----------
    n_pregunta: int
        El número de la pregunta actual.
    p_level: int
        La cantidad de preguntas por nivel (puede ser 2 o 3).
    
    Returns
    -------
    level: str
        El nivel de dificultad seleccionado: 'basicas', 'intermedias' o 'avanzadas'.
    """
    if 1 <= n_pregunta <= p_level:
        level = "basicas"
    elif p_level < n_pregunta <= 2 * p_level:
        level = "intermedias"
    else:
        level = "avanzadas"

    return level
