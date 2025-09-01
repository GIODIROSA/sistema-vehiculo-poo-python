from vehiculo import Vehiculo


class Moto(Vehiculo):
    def __init__(self, marca, modelo, precio, cilindrada):
        super().__init__(marca, modelo, precio)
        self.cilindrada = cilindrada

    def get_precio_moto(self):
        return self.get_precio()
    
    def set_precio_moto(self, nuevo_precio_moto):
        if nuevo_precio_moto > 0:
            self.set_precio(nuevo_precio_moto)
        else:
            print("El precio de la moto debe ser mayor que 0")

    
    def descripcion(self):
        valor_precio = self.get_precio_moto()
        objeto_descripcion_moto= {
            "marca": self.marca,
            "modelo": self.modelo,
            "precio": valor_precio,
            "cilindrada": self.cilindrada
         }
        return f"-Descripción de la Moto | marca: {objeto_descripcion_moto['marca']}, modelo: {objeto_descripcion_moto["modelo"]}, precio: {objeto_descripcion_moto['precio']}, cilindrada: {objeto_descripcion_moto['cilindrada']} cc"


