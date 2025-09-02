class Familia:
    def __init__(self, nombre, tarifa_energia):
        self.nombre = nombre
        self.tarifa_energia = tarifa_energia
        self.electrodomesticos = []

    def agregar_electrodomestico(self, electrodomestico):
        self.electrodomesticos.append(electrodomestico)

    def resumen_consumo(self):
        total_energia = sum(i.consumo_mensual() for i in self.electrodomesticos)
        total_costo = sum(i.costo_mensual(self.tarifa_energia) for i in self.electrodomesticos)
        return f"Familia {self.nombre} - Total: {total_energia:.2f} energia electrica, Costo: ${total_costo:.2f}"