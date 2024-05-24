class Empleado:
    def pedir_nombre(self):
        self.nombre = input("Ingrese el nombre del empleado: ")

class Salario:
    def pedir_salario(self):
        self.salario = float(input("Ingrese el salario del empleado: "))

class Designacion(Empleado, Salario):
    def __init__(self):
        super().__init__()

    def designar_cargo(self, cargo):
        self.cargo = cargo
        print(f"El empleado {self.nombre} ha sido designado como {self.cargo}.")

# Instanciación y verificación
empleado_designado = Designacion()
empleado_designado.pedir_nombre()
empleado_designado.pedir_salario()

empleado_designado.designar_cargo("Gerente")

if hasattr(empleado_designado, 'nombre') and hasattr(empleado_designado, 'salario'):
    print("El objeto tiene los atributos 'nombre' y 'salario'.")
else:
    print("El objeto no tiene los atributos 'nombre' y 'salario'.")
