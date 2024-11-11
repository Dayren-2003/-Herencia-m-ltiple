from classDepartamento import Departamento

class Area(Departamento):
    def __init__(self):
        super().__init__()
        self._descripcion =  ""
        self._departamentos= ""

        # Getters y Setters

    def get_descirpcion(self):
        return self._descripcion

    def set_descripcion(self, descripcion):
        self._descricion = descripcion

    def get_departamentos(self):
        return self._departamentos

    def set_departamentos(self, departamentos):
        self._departamentos = departamentos

    def mostrar_informacion(self):
        return f" descripcion: {self._descricion}, departamentos: {self._departamentos}"