from Electrodomesticos import Electrodomestico
from familias_sv import Familia

familia1 = Familia("Ramírez", tarifa_energia=0.20)

#electrodomésticos
refri = Electrodomestico("Refrigeradora", 0.15, 720)
tv = Electrodomestico("Televisor", 0.10, 120)
ac = Electrodomestico("Aire Acondicionado", 1.5, 90)
luces = Electrodomestico("Iluminación", 0.05, 300)

for i in Electrodomestico.listado:
    familia1.agregar_electrodomestico(i)

print(familia1.resumen_consumo())
print("\n Detalle por electrodoméstico:")
for i in familia1.electrodomesticos:
    print(i.datos(familia1.tarifa_energia))