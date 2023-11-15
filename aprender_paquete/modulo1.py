class Cliente:

    def __init__(self, nombre, correo, edad, intereses):
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.intereses = intereses
    
    def compra(self, producto, tienda, ubicacion):
        self.producto = producto
        self.tienda = tienda
        self.ubicacion = ubicacion
        print(
            f"{self.nombre} ha comprado un {self.producto} en nuestra tienda de {self.ubicacion} a la edad de {self.edad}, le haremos entrega de su boleta al correo {self.correo}, gracias por su compra. "
        )
    def __str__(self):
        return f"fue creado el cliente {self.nombre}."



        
        