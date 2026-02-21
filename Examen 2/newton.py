def metodo_newton_raphson(func, dfunc, x0, tol=1e-5, max_iter=100):
    """
    Implementación del método de Newton-Raphson.
    Parámetros:
    dfunc: derivada de la función
    x0: valor inicial
    """
    print(f"{'Iter':<5} {'xi':<15} {'Error est.':<15}")

    xi = x0
    for i in range(max_iter):
        fx = func(xi)
        dfx = dfunc(xi)

        if dfx == 0:
            print("Error: Derivada cero. No se puede continuar.")
            return None

        xi_next = xi - (fx / dfx)

        if xi_next != 0:
            ea = abs((xi_next - xi) / xi_next) * 100
        else:
            ea = 0

        print(f"{i+1:<5} {xi_next:<15.8f} {ea:<15.8f}%")

        if ea < tol:
            return xi_next

        xi = xi_next

    return xi
