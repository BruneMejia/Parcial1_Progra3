class Familia:
    def __init__(self, nombre, tarifa_kwh):
        self.nombre = nombre
        self.tarifa_kwh = tarifa_kwh
        self.electrodomesticos = []

    def agregar_electrodomestico(self, electrodomestico):
        self.electrodomesticos.append(electrodomestico)

    def resumen_consumo(self):
        total_kwh = sum(e.consumo_mensual() for e in self.electrodomesticos)
        total_costo = sum(e.costo_mensual(self.tarifa_kwh) for e in self.electrodomesticos)
        return f"Familia {self.nombre} - Total: {total_kwh:.2f} kWh, Costo: ${total_costo:.2f}"