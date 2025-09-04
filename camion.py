from vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, marca, modelo, precio, capacidad_carga):
        super().__init__(marca, modelo, precio)
        if capacidad_carga >= 1000:
            self.capacidad_carga = capacidad_carga
        else:
            print("El camión debe tener una capacidad de carga mínima de 1000 kg")
            self.capacidad_carga = 1000

    #Trae el precio
    def get_precio_camion(self):
        return self.get_precio()
    
    #Modifica el precio
    def set_precio_camion(self, nuevo_precio_camion):
        if nuevo_precio_camion > 0:
            self.set_precio(nuevo_precio_camion)
        else:
            print("El precio del camión debe ser mayor que 0")

    #Metodo arma la descripción del vehiculo
    def descripcion(self):
        valor_precio_camion = self.get_precio_camion()
        objeto_descripcion_camion= {
            "marca": self.marca,
            "modelo": self.modelo,
            "precio": valor_precio_camion,
            "capacidad_carga": self.capacidad_carga
        }
        return f"-Descripción del Camión | marca {objeto_descripcion_camion['marca']}, modelo {objeto_descripcion_camion['modelo']}, precio ${objeto_descripcion_camion['precio']}, capacidad de carga {objeto_descripcion_camion['capacidad_carga']} kg"
    

    