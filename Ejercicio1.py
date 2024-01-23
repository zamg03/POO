#Crear una clase estudiante con los atributos Nombre, Edad y Grado. 
#Agregar un metodo Estudiar(), que imprima 'El estudiante (nombre) esta estudiando'.
#Pedir nombre, edad y grado al usuario y mostrar los datos de la clase.

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print('Estudiando...')

nombre = input('Ingresa tu nombre: ')
edad = int(input('Ingresa tu edad: '))
grado = input('Ingresa tu grado: ')

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ESTUDIANTE \n\n
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Grado: {estudiante.grado} \n

      """)

while True:
    estudiar = input()
    if (estudiar.lower() == 'estudiar'):
        estudiante.estudiar()