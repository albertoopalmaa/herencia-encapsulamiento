from abc import ABC, abstractmethod


class Vuelos:
    def __init__(self, numero_vuelo, destino, duracion):
        self.numero_vuelo = numero_vuelo
        self.destino = destino
        self.duracion = duracion

    @abstractmethod
    def obtener_detalles(self):
        pass

    @abstractmethod
    def precio(self):
        pass


class VuelosNacionales (Vuelos):
    def __init__(self, numero_vuelo, destino, duracion, tarifa_base):
        super().__init__(numero_vuelo, destino, duracion)
        self.__tarifa_base = tarifa_base

    def obtener_detalles(self):
        return f"Vuelo Nacional {self.numero_vuelo} a {self.destino} con duracion {self.duracion} horas"

    def precio(self):
        return f"El precio es {self.__tarifa_base} pesos"


class VuelosInternacionales (Vuelos):
    def __init__(self, numero_vuelo, destino, duracion, tarifa_base, impuestos):
        super().__init__(numero_vuelo, destino, duracion)
        self.__tarifa_base = tarifa_base
        self.__impuestos = impuestos

    def obtener_detalles(self):
        return f"Vuelo Internacional {self.numero_vuelo} a {self.destino} con duracion {self.duracion} horas"

    def precio(self):
        return f"El precio es {self.__tarifa_base + self.__impuestos} pesos"