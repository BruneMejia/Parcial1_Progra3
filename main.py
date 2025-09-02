from Electrodomesticos import Electrodomestico
from familias_sv import Familia

familia1 = Familia("Ramírez", tarifa_energia=0.20)
#electrodomésticos
refri = Electrodomestico("Refrigeradora", 0.15, 720)
tv = Electrodomestico("Televisor", 0.10, 120)
ac = Electrodomestico("Aire Acondicionado", 1.5, 90)
luces = Electrodomestico("Iluminación", 0.05, 300)

familia1.agregar_electrodomestico(refri)
familia1.agregar_electrodomestico(tv)
familia1.agregar_electrodomestico(ac)
familia1.agregar_electrodomestico(luces)

#familia 2
familia2 = Familia("López", tarifa_energia=0.18)
refri2 = Electrodomestico("Refrigeradora", 0.12, 600)
tv2 = Electrodomestico("Televisor", 0.08, 150)
ventilador2 = Electrodomestico("Ventilador", 0.06, 200)

familia2.agregar_electrodomestico(refri2)
familia2.agregar_electrodomestico(tv2)
familia2.agregar_electrodomestico(ventilador2)

# familia 3
familia3 = Familia("Martínez", tarifa_energia=0.22)
ac3 = Electrodomestico("Aire Acondicionado", 1.2, 100)
luces3 = Electrodomestico("Iluminación", 0.04, 250)

familia3.agregar_electrodomestico(ac3)
familia3.agregar_electrodomestico(luces3)

familias = [familia1, familia2, familia3]

#datos
for familia in familias:
    print("\n" + familia.resumen_consumo())
    print(" Electrodomésticos:")
    for elec in familia.electrodomesticos:
        print("  " + elec.datos(familia.tarifa_energia))
