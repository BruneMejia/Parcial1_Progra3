class Electrodomestico:
    listado = []

    def __init__(self, nombre, consumo_por_hora, horas_uso_mensual):
        self.nombre = nombre
        self.consumo_por_hora = consumo_por_hora 
        self.horas_uso_mensual = horas_uso_mensual
        Electrodomestico.listado.append(self)

    def consumo_mensual(self):
        return self.consumo_por_hora * self.horas_uso_mensual

    def costo_mensual(self, precio_por_energia):
        return self.consumo_mensual() * precio_por_energia

    def datos(self, precio_por_energia):
        return (f"{self.nombre}: {self.consumo_mensual():.2f} energia electrica, "
                f"Total de gasto del electrodomestico: ${self.costo_mensual(precio_por_energia):.2f}")