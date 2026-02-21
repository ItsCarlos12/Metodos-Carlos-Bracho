def metodo_falsa_posicion(func, a, b, tol=1e-5, max_iter=100):
    """Implementación del método de Falsa Posición.

    Devuelve la raíz estimada y el error aproximado en la
    segunda iteración (en porcentaje).
    """
    if func(a) * func(b) >= 0:
        print("Error: f(a) y f(b) deben tener signos opuestos.")
        return None, None

    xr_old = a
    ea_iter2 = None

    for i in range(max_iter):
        # Fórmula de la Falsa Posición
        xr = b - (func(b) * (a - b)) / (func(a) - func(b))

        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100
        else:
            ea = 0.0

        # Guardar error aproximado en la iteración 2 (i = 1)
        if i == 1:
            ea_iter2 = ea

        if abs(func(xr)) < tol or ea < tol:
            return xr, ea_iter2

        if func(a) * func(xr) < 0:
            b = xr
        else:
            a = xr

        xr_old = xr

    return xr, ea_iter2
