def metodo_biseccion(func, a, b, tol=1.0, max_iter=100):
    """Implementación del método de Bisección.

    Parámetros
    ----------
    func : callable
        Función a evaluar.
    a, b : float
        Límites del intervalo inicial.
    tol : float
        Tolerancia del error relativo porcentual (por defecto 1.0 = 1%).
    max_iter : int
        Número máximo de iteraciones.

    Returns
    -------
    root : float | None
        Raíz estimada.
    iteraciones : int
        Número de iteraciones realizadas.
    criterio : str
        Criterio de convergencia alcanzado.
    subintervalo : tuple[float, float]
        Sub-intervalo final [a, b] que contiene la raíz.
    """
    fa = func(a)
    fb = func(b)
    if fa * fb >= 0:
        print("El método de bisección falló. f(a) y f(b) deben tener signos opuestos.")
        return None, 0, "f(a) y f(b) sin signos opuestos", (a, b)

    print(f"{'Iter':<5} {'a':<10} {'b':<10} {'xr':<10} {'Error est.':<10}")

    xr_old = a
    criterio = "No convergió en max_iter"

    for i in range(1, max_iter + 1):
        xr = (a + b) / 2.0

        # Cálculo del error aproximado relativo porcentual
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100.0
        else:
            ea = 0.0

        print(f"{i:<5} {a:<10.5f} {b:<10.5f} {xr:<10.5f} {ea:<10.5f}%")

        fxr = func(xr)

        if abs(fxr) < 1e-12:
            criterio = "f(xr) ≈ 0"
            return xr, i, criterio, (a, b)

        if ea < tol and i > 1:
            criterio = f"ea < {tol}%"
            return xr, i, criterio, (a, b)

        # Actualización del subintervalo
        if fa * fxr < 0:
            b = xr
            fb = fxr
        else:
            a = xr
            fa = fxr

        xr_old = xr

    return xr, max_iter, criterio, (a, b)
