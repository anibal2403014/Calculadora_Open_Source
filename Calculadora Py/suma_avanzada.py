def suma_avanzada(numeros):
    # Verifica que la lista no esté vacía
    if len(numeros) == 0:
        return "Error: La lista de números está vacía."

    # Verifica que todos los elementos sean numéricos
    if not all(isinstance(num, (int, float)) for num in numeros):
        return "Error: Todos los elementos de la lista deben ser números."

    # Retorna la suma de los números
    return sum(numeros)
