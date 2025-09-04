# En tu archivo principal

from vehiculo import Vehiculo
from moto import Moto
from auto import Auto
from camion import Camion
from concesionario import Concesionario 

# Crear una instancia del concesionario
concesionario = Concesionario()

def main():
    # Crear instancias de vehículos
    vehiculo = Vehiculo("Toyota", "Corolla", 20000)
    moto = Moto("Honda", "CBR600RR", 15000, 600)
    auto = Auto("Ford", "EcoSport station Wagon", 15000, 5)
    camion = Camion("Volvo", "FH16", 120000, 2000)
    auto_chevrolet = Auto("Chevrolet", "Camaro", 25000, 4)

    # 1. Agregar vehículos al concesionario
    concesionario.agregar_vehiculo(vehiculo)
    concesionario.agregar_vehiculo(moto)
    concesionario.agregar_vehiculo(auto)
    concesionario.agregar_vehiculo(camion)
    concesionario.agregar_vehiculo(auto_chevrolet)

    # 2. Mostrar descripciones individuales
    # Se realiza polimorfismo en el uso de descripción
    print("\n--- Descripciones Individuales ---")
    print(vehiculo.descripcion())
    print(moto.descripcion())
    print(auto.descripcion())
    print(camion.descripcion())

    # 3. Mostrar el catálogo completo antes de la modificación
    print("\n--- Catálogo ANTES de la modificación ---")
    concesionario.mostrar_catalogo()

    # 4. Modificar el precio de un vehículo
    print("\n--- Modificando el precio de un vehículo ---")
    concesionario.modificar_precio_vehiculo(auto_chevrolet, 1235000)

    # 5. Mostrar el catálogo completo después de la modificación
    print("\n--- Catálogo DESPUÉS de la modificación ---")
    concesionario.mostrar_catalogo()


if __name__ == "__main__":
    main()