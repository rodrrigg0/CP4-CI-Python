def es_primo(numero: int) -> bool:
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    limite = int(numero ** 0.5) + 1
    for n in range(3, limite, 2):
        if numero % n == 0:
            return False
    return True
