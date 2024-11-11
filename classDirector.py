from classArea import Area
from classEmpleado import Empleado

class Director(Area,Empleado):
    def __init__(self):
        super().__init__()
        self._contratacion = ""
        self._salario = ""

    # Getters y Setters
    def get_contratacion(self):
        return self._contratacion

    def set_contratacion(self, contratacion):
        self._contratacion = contratacion

    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        self._salario = salario

    def mostrar_informacion(self):
        return f"Contratacion: {self._contratacion}, salario: {self._salario}"