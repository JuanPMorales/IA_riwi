def ordenar_tres_numeros(a, b, c, descendente=False):
    """Ordena tres números mediante comparaciones e intercambios."""
    # Primero se ordenan A y B para que B sea el mayor de los dos.
    if a > b:
        a, b = b, a

    # Se compara el mayor de los dos primeros números con C.
    if b > c:
        b, c = c, b

    # Si C ocupó el lugar de B, se verifica nuevamente el orden inicial.
    if a > b:
        a, b = b, a

    orden = (a, b, c)
    return orden[::-1] if descendente else orden


def main():
    numeros = input("Ingrese tres números separados por espacios: ").split()
    if len(numeros) != 3:
        raise ValueError("Debe ingresar exactamente tres números.")

    try:
        a, b, c = (float(numero) for numero in numeros)
    except ValueError as error:
        raise ValueError("Todos los valores deben ser números.") from error

    direccion = input("¿Orden ascendente o descendente? ").strip().lower()
    if direccion not in ("ascendente", "descendente"):
        raise ValueError("La dirección debe ser 'ascendente' o 'descendente'.")

    resultado = ordenar_tres_numeros(
        a, b, c, descendente=direccion == "descendente"
    )
    print("Orden final:", " ".join(str(numero) for numero in resultado))


if __name__ == "__main__":
    main()