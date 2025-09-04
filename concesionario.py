from vehiculo import Vehiculo

class Concesionario:
    def __init__(self):
        self.catalogo = []

    #Metodo para agregar el vehiculo al catálogo
    def agregar_vehiculo(self, vehiculo):
        print(f"Vehículo agregado: {vehiculo.descripcion()} - Precio: ${vehiculo.get_precio()}")
        self.catalogo.append(vehiculo)   

    #Metodo para modificar el precio del vehiculo
    def modificar_precio_vehiculo(self, vehiculo_a_modificar, nuevo_precio): 
        for vehiculo in self.catalogo:
            if vehiculo is vehiculo_a_modificar:
                print(f"Modificando precio del vehiculo: vehiculo {vehiculo.descripcion()}")
                print(f"Precio anterior: ${vehiculo.get_precio()}")
                vehiculo.set_precio(nuevo_precio)
                print(f"Nuevo precio: ${vehiculo.get_precio()}")
                return
            
            
    #Metodo para mostrar el catalogo
    def mostrar_catalogo(self):
        print("\n--- Catálogo de Vehículos ---")
        print("Total de vehículos en el concesionario:", len(self.catalogo))
        print("----------------------------")
        print("CATÁLOGO DE VEHÍCULOS:")
        total = 0
        for index, vehiculo in enumerate(self.catalogo):
            print(f"({index + 1}) {vehiculo.descripcion()} | Precio-lista: ${vehiculo.get_precio()}")
            total += vehiculo.get_precio()
        print(f"Total del valor de los vehículos: ${total}")


