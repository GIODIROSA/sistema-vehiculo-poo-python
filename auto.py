from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, modelo, precio, puertas):
        super().__init__(marca, modelo, precio)
        if puertas >= 2:
            self.puertas = puertas
        else:
            print("El auto debe tener al menos 2 puertas")
            self.puertas = 2

    #Trae el precio
    def get_precio_auto(self):
        return self.get_precio()
    
    #Modifica el precio
    def set_precio_auto(self, nuevo_precio_auto):
        if nuevo_precio_auto > 0:
            self.set_precio(nuevo_precio_auto)
        else:
            print("El precio del auto debe ser mayor que 0")

     #Metodo arma la descripción del vehiculo
    def descripcion(self):
        precio_moto = self.get_precio_auto()
        objeto_descripcion_auto = {
            "marca": self.marca,
            "modelo": self.modelo,
            "precio": precio_moto,
            "puertas": self.puertas
        }
        
        return f"-Descripción del Auto | marca: {objeto_descripcion_auto['marca']}, modelo: {objeto_descripcion_auto['modelo']}, precio: {objeto_descripcion_auto['precio']}, puertas: {objeto_descripcion_auto['puertas']}"
    
