class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Estas haciendo la llamada desde un: {self.modelo}")

    def cortar(self):
        print(f"Cortaste la llamada desde tu: {self.modelo}")

Celular1 = Celular("Samsung","S23","48MP")
Celular2 = Celular("Apple","Iphone 15 Pro","96MP")

Celular2.llamar()