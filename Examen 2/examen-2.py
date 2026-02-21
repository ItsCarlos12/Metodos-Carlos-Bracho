from functions import f_biseccion, f_regula, f_newton, df_newton, f_secante
from metodo_biseccion import metodo_biseccion
from newton import metodo_newton_raphson
from regula_falsi import metodo_falsa_posicion
from sec import metodo_secante


def main():
    tol_bis = 0.1   
    tol_otros = 1e-5
    max_iter = 100

    print("\n=== Método de Bisección ===")
    # Intervalo donde f_biseccion cambia de signo: entre 5 y 6
    raiz_bis, it_bis, criterio_bis, sub_bis = metodo_biseccion(
        f_biseccion, 5.0, 6.0, tol=tol_bis, max_iter=max_iter
    )
    print("\n--- Resumen Bisección ---")
    print(f"Raíz estimada: {raiz_bis}")
    print(f"Iteraciones hasta ea < 1%: {it_bis}\n")

    print("\n=== Método de Falsa Posición (Regula Falsi) ===")
    # Intervalo sugerido en el enunciado: [0, 100]
    raiz_rf, ea_iter2 = metodo_falsa_posicion(
        f_regula, 0.0, 100.0, tol=tol_otros, max_iter=max_iter
    )
    print("\n--- Resumen Regula Falsi ---")
    print(f"Tiempo calculado t (raíz): {raiz_rf}")
    print(f"Error aproximado en iteración 2: {ea_iter2}%\n")

    print("\n=== Método de Newton-Raphson ===")
    # Valor inicial cercano a la raíz (entre 1 y 4)
    raiz_nr = metodo_newton_raphson(
        f_newton, df_newton, 3.0, tol=tol_otros, max_iter=max_iter
    )
    print("\n--- Resumen Newton-Raphson ---")
    print(f"Reactancia crítica x (raíz): {raiz_nr}")
    print(f"Valor de f'(x) en x = 2: {df_newton(2.0)}\n")

    print("\n=== Método de la Secante ===")
    # Valores iniciales solicitados: x0 = 1, x1 = 1.5
    raiz_sec, x_siguiente = metodo_secante(
        f_secante, 1.0, 1.5, tol=tol_otros, max_iter=max_iter
    )
    print("\n--- Resumen Secante ---")
    print(f"Resistencia R (raíz): {raiz_sec}")
    print(f"Siguiente x calculada (a partir de x0=1, x1=1.5): {x_siguiente}\n")


if __name__ == "__main__":
    main()
