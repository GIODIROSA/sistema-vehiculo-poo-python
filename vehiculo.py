
class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.__precio = precio

    def get_precio(self): 
            mostrar_precio = self.__precio
            return mostrar_precio
    
    def set_precio(self, nuevo_precio):
            if nuevo_precio > 0:
                self.__precio = nuevo_precio
                print(f"El nuevo precio es: {self.__precio}")
            else:
                print("El precio debe ser mayor que 0")

    def descripcion(self):   
         objeto_descripcion= {
            "marca": self.marca,
            "modelo": self.modelo,
            "precio": self.__precio
         }
         return f"-Descripción del Vehiculo | marca: {objeto_descripcion['marca']}, modelo: {objeto_descripcion['modelo']}, precio: {objeto_descripcion['precio']}"





    





    
