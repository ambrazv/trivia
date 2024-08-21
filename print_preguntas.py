import preguntas as p


def print_pregunta(enunciado, alternativas):
    """
    Imprime una pregunta con su enunciado y sus alternativas numeradas.

    Parámetros:
    enunciado (str): El texto del enunciado de la pregunta.
    alternativas (list): Lista de alternativas a la pregunta.

    Retorno:
    None
    """
    # Imprimir el enunciado
    print(enunciado)
    print()  # Salto de línea

    # Imprimir cada alternativa con su letra asociada
    letras = ["A", "B", "C", "D"]
    for i, alternativa in enumerate(alternativas):
        print(f"{letras[i]}. {alternativa[0]}")


if __name__ == "__main__":
    # Obtener la pregunta del pool de preguntas
    pregunta = p.pool_preguntas["basicas"]["pregunta_1"]

    # Imprimir la pregunta y sus alternativas
    print_pregunta(pregunta["enunciado"], pregunta["alternativas"])
