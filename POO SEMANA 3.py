class ClimaDiario:
    def __init__(self):
        self.temperaturas = []
    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)
    def calcular_promedio(self):
        suma = sum(self.temperaturas)
        promedio = suma / len(self.temperaturas)
        return promedio
# Clase principal
class ClimaSemanal:
    def __init__(self):
        self.clima_diario = ClimaDiario()
    def ejecutar(self):
        self.clima_diario.ingresar_temperaturas()
        promedio = self.clima_diario.calcular_promedio()
        print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")
# Crear una instancia de ClimaSemanal y ejecutar el programa
if __name__ == "__main__":
    clima_semanal = ClimaSemanal()
    clima_semanal.ejecutar()