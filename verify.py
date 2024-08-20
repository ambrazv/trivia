import preguntas as p


def verificar(alternativas, eleccion):
    """Verifica si la elección del usuario es correcta basándose en las alternativas dadas.
    Parámetros
    ----------
    alternativas : list of list
        Lista de listas, donde cada sublista contiene una alternativa y un valor indicativo de su correción(1 para correcta, 0 para incorrecta)
    eleccion: str
        La opción seleccionada del usuario ('a','b','c','d').
    Returns
    -------
    Correcto: booleano
        True si la elección es correcta, False en caso contrario.
    """

    # devuelve el índice de elección dada
    eleccion = ["a", "b", "c", "d"].index(eleccion)

    # generar lógica para determinar respuestas correctas
    # Determinar si la respuesta es correcta
    correcto = alternativas[eleccion][1] == 1

    if correcto:
        print("Respuesta Correcta")
    return correcto


if __name__ == "__main__":
    from print_preguntas import print_pregunta

    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas["basicas"]["pregunta_2"]
    print_pregunta(pregunta["enunciado"], pregunta["alternativas"])
    respuesta = input("Escoja la alternativa correcta:\n> ").lower()
    verificar(pregunta["alternativas"], respuesta)
