class Electrodomestico:
    listado = []

    def _init_(self, nombre, consumo_por_hora, horas_uso_mensual):
        self.nombre = nombre
        self.consumo_por_hora = consumo_por_hora 
        self.horas_uso_mensual = horas_uso_mensual
        Electrodomestico.listado.append(self)

    def consumo_mensual(self):
        return self.consumo_por_hora * self.horas_uso_mensual

    def costo_mensual(self, precio_por_kwh):
        return self.consumo_mensual() * precio_por_kwh

    def info(self, precio_por_kwh):
        return (f"{self.nombre}: {self.consumo_mensual():.2f} kWh, "
                f"Costo: ${self.costo_mensual(precio_por_kwh):.2f}")