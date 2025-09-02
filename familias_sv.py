class Familia:
    def __init__(self, nombre, tarifa_energia):
        self.nombre = nombre
        self.tarifa_energia = tarifa_energia
        self.electrodomesticos = []
#Manda a llamar a los electrodomesticos
    def agregar_electrodomestico(self, electrodomestico):
        self.electrodomesticos.append(electrodomestico)
#Muestra el consumo mensusal de energia de las fomilias y el total a pagar
    def resumen_consumo(self):
        total_energia = sum(i.consumo_mensual() for i in self.electrodomesticos)
        total_costo = sum(i.costo_mensual(self.tarifa_energia) for i in self.electrodomesticos)
        return f"Familia {self.nombre} - Total: {total_energia:.2f} de energia electrica, Total a pagar: ${total_costo:.2f}"