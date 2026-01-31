import csv
import functions

def main():
    valores_reales = []
    sensores = {"Sensor_A": [], "Sensor_B": [], "Sensor_C": []}

    # Leer datos desde el archivo CSV
    with open("Data_Calibracion_29877307.csv", "r") as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            valores_reales.append(float(fila["Presion_Patron_PSI"]))
            sensores["Sensor_A"].append(float(fila["Sensor_A_PSI"]))
            sensores["Sensor_B"].append(float(fila["Sensor_B_PSI"]))
            sensores["Sensor_C"].append(float(fila["Sensor_C_PSI"]))

    # Procesar cada sensor
    for sensor, valores_medidos in sensores.items():
        suma_error_absoluto = 0
        max_error_absoluto = float('-inf')
        suma_error_relativo = 0

        for valor_real, valor_medido in zip(valores_reales, valores_medidos):
            error_absoluto, error_relativo = functions.calcular_errores(valor_real, valor_medido)
            suma_error_absoluto += error_absoluto
            max_error_absoluto = max(max_error_absoluto, error_absoluto)
            suma_error_relativo += error_relativo

        promedio_error_relativo = suma_error_relativo / len(valores_reales)
        promedio_error_relativo_porcentual = promedio_error_relativo * 100

        print(f"\nResultados para {sensor}:")
        print(f"Suma de errores absolutos: {suma_error_absoluto}")
        print(f"Máximo error absoluto: {max_error_absoluto}")
        print(f"Promedio de errores relativos: {promedio_error_relativo}")
        print(f"Promedio de errores relativos porcentual: {promedio_error_relativo_porcentual}%")

if __name__ == "__main__":
    main()