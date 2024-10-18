from clases_vuelos import *


def gestor_de_vuelos():
    vuelo_nacional = VuelosNacionales("AAA123", "Bariloche", 2, 200.00)
    vuelo_internacional = VuelosInternacionales(
        "AAA654", "Barcelona", 16, 500.00, 100.00)

    print(vuelo_nacional.obtener_detalles())
    print(vuelo_nacional.precio())

    print(vuelo_internacional.obtener_detalles())
    print(vuelo_internacional.precio())

if __name__ == "__main__":
    gestor_de_vuelos()
