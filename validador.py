def validate(opciones, eleccion):
    """Valida que la elección del usuario esté dentro de las opciones.
    Parámetros
    ----------
    opciones: list of str
        Lista de opciones válidas que el usuario puede seleccionar.
    elección: str
        Es la opción seleccionada por el usuario
    Returns
    -------
    str
        La opción validada que ha sido ingresada correctamente.
    """
    while eleccion not in opciones:
        eleccion = input(
            f"Opción no válida, ingrese una de las opciones válidas: {opciones}\n> "
        ).lower()
    return eleccion


if __name__ == "__main__":

    eleccion = input("Ingresa una Opción: ").lower()
    letras = [
        "a",
        "b",
        "c",
        "d",
    ]  # pueden probar con letras también para verificar su funcionamiento.
    numeros = ["0", "1"]
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
