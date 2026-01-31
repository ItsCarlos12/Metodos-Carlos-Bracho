def calcular_errores(valor_real, valor_medido):

    # Error Absoluto
    error_absoluto = abs(valor_real - valor_medido)

    # Error Relativo
    if valor_real != 0:
        error_relativo = error_absoluto / abs(valor_real)
    else:
        error_relativo = float('inf')  # Indefinido o infinito si el valor real es cero

    return error_absoluto, error_relativo



