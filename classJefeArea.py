from classArea import Area
from classEmpleado import Empleado

class JefeArea(Area, Empleado):
    def __init__(self):
        super().__init__()
        self._supervisados= ""
        self._nivel_jerarquico = ""

    # Getters y Setters
    def get_supervisados(self):
        return self._supervisados

    def set_supervisados(self, supervisados):
        self._supervisados = supervisados

    def get_nivel_jerarquico(self):
        return self._nivel_jerarquico

    def set_nivel_jerarquico(self, nivel_jerarquico):
        self._nivel_jerarquico= nivel_jerarquico

    def mostrar_informacion(self):
        return f"supervisados: {self._supervisados}, nivel_jerarquico: {self._nivel_jerarquico}"