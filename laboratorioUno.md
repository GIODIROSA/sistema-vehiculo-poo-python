Laboratorio N.° 1: Sistema de Vehículos

📝 Objetivo

Aplicar los conceptos fundamentales de la Programación Orientada a Objetos (POO) en Python, tales como:

    Herencia

    Polimorfismo

    Encapsulamiento

    Uso de clases principales que gestionan instancias de objetos

🚗 Contexto

Una concesionaria de vehículos necesita un sistema para registrar y mostrar la información de distintos tipos de vehículos, como autos, motos y camiones.

📜 Instrucciones

Clases a crear

    Vehiculo (Clase Base)

        Atributos: marca, modelo y __precio (atributo encapsulado).

        Métodos:

            get_precio(): Retorna el precio del vehículo. check

            set_precio(nuevo_precio): Cambia el precio solo si nuevo_precio es mayor que 0. check

            descripcion(): Devuelve un texto general, por ejemplo: "Vehículo marca X, modelo Y".

    Clases Hijas (heredan de Vehiculo)

        Auto: Atributo adicional puertas.

        Moto: Atributo adicional cilindrada.

        Camion: Atributo adicional capacidad_carga.

        Polimorfismo: Cada clase debe sobrescribir el método descripcion() para mostrar sus datos específicos.

    Concesionaria

        Atributo: Una lista para almacenar los vehículos.

        Métodos:

            agregar_vehiculo(vehiculo): Añade una instancia de vehículo a la lista.

            mostrar_catalogo(): Recorre la lista, muestra la descripción y el precio de cada vehículo, y calcula el total de la concesionaria.

Programa principal (main)

    Crea una instancia de la clase Concesionaria.

    Instancia al menos un auto, una moto y un camión.

    Utiliza el método setter para modificar el precio de uno de los vehículos.

    Agrega todos los vehículos a la concesionaria.

    Muestra el catálogo completo.

💬 Comentarios y Documentación

Es indispensable agregar comentarios claros en el código para:

    Explicar la función de cada método.

    Indicar la relación entre las clases Padre e Hijo.

    Señalar dónde se aplica el polimorfismo.

    Describir las acciones realizadas en el programa principal (main).

📦 Entrega

    Suba su aplicación comprimida en formato .RAR o .7ZIP a la sección de tareas (Laboratorio Uno).

    Asegúrese de que el archivo comprimido contenga todo su desarrollo y clases.

    Considere el material revisado en clases.

    La fecha límite de entrega se encuentra en la sección de avisos del curso.

📊 Escala de Apreciación

Criterio	Logro Alto (3 puntos)	Logro Medio (2 puntos)	Logro Inicial (1 punto)
Clase base Vehiculo	Define correctamente atributos y métodos, incluyendo el encapsulamiento.	Define la clase, pero con errores parciales o mal uso de get/set.	Clase incompleta o sin encapsulamiento del atributo precio.
Clases hijas	Heredan, agregan atributos propios y sobrescriben descripcion() correctamente.	Heredan, pero con errores en atributos adicionales o sin sobrescribir el método.	No implementa herencia o el método descripcion() es incorrecto.
Encapsulamiento	Implementa getters y setters correctamente, validando el precio.	Usa get/set pero sin validaciones adecuadas o con errores en la lógica.	No aplica encapsulamiento o manipula el precio directamente.
Clase Concesionaria	Implementa la lista, agrega vehículos y muestra el catálogo con el total.	Implementa parcialmente (agrega vehículos, pero el catálogo está incompleto o sin total).	No implementa la clase Concesionaria o no funciona.
Programa principal (main)	Crea la concesionaria, instancia vehículos, modifica el precio con el setter y muestra el catálogo.	Instancia vehículos, pero no aplica correctamente el setter o el catálogo.	No logra integrar los vehículos en el programa principal.
Comentarios	Incluye comentarios claros y completos.	Incluye algunos comentarios, pero son incompletos o poco claros.	Carece de comentarios o son irrelevantes.

Puntaje total: 18 puntos

