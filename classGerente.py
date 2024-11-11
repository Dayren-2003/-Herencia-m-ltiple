from classArea import Area
from classEmpleado import Empleado

class Gerente(Area, Empleado):
    def __init__(self):
        super().__init__()
        self._telefono = ""
        self._nivel_gerencial = ""

    # Getters y Setters
    def get_telefono(self):
        return self._nivel_gerencial

    def set_telefono(self, telefono):
        self._telefono = telefono

    def get_nivel_gerencial(self):
        return self._nivel_gerencial

    def set_nivel_gerencial(self, nivel_gerencial):
        self._nivel_gerencial = nivel_gerencial

    def mostrar_informacion(self):
        return f"telefono: {self._telefono},nivel_gerencial: {self._nivel_gerencial}"