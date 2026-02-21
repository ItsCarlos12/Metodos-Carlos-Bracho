def metodo_secante(func, x0, x1, tol=1e-5, max_iter=100):
    """Implementación del método de la Secante.

    Devuelve la raíz estimada y el valor de x
    obtenido en la primera iteración (x2) para
    los puntos iniciales dados.
    """

    print(f"{'Iter':<5} {'xi+1':<15} {'Error est.':<15}")

    primera_x = None

    for i in range(max_iter):
        f_x0 = func(x0)
        f_x1 = func(x1)

        if f_x1 - f_x0 == 0:
            print("Error: División por cero.")
            return None, primera_x

        # Fórmula de la Secante
        x_next = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)

        if x_next != 0:
            ea = abs((x_next - x1) / x_next) * 100
        else:
            ea = 0.0

        print(f"{i+1:<5} {x_next:<15.8f} {ea:<15.8f}%")

        # Guardar la primera x calculada (x2 cuando partimos de x0, x1)
        if i == 0:
            primera_x = x_next

        if ea < tol:
            return x_next, primera_x

        
        x0 = x1
        x1 = x_next

    return x_next, primera_x
