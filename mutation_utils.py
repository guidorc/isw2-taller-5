import random
import string


def insert_random_character(s: str) -> str:
    """Retorna s con un caracter random insertado en una posicion al azar"""
    length = len(s)
    if length == 0:
        return random.choice(string.printable)

    index = random.randint(0, length - 1)
    character = random.choice(string.printable)
    prefix = s[:index]
    suffix = s[index:]

    return prefix + character + suffix


def delete_random_character(s: str) -> str:
    """Retorna s con un caracter random eliminado.
    Si la cadena esta vacia, no la modifica"""
    length = len(s)

    if length == 0:
        return s

    index = random.randint(0, length - 1)
    return s[:index] + s[index + 1:]


def change_random_character(s: str) -> str:
    """Retorna s con un caracter modificado en una posicion al azar.
    El caracter a modificar es reemplazado por otro caracter random.
    Si la cadena esta vacia, no la modifica."""
    length = len(s)

    if length == 0:
        return s

    index = random.randint(0, length - 1)
    character = random.choice(string.printable)

    s_as_list = list(s)
    s_as_list[index] = character
    return "".join(s_as_list)
