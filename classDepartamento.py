class Departamento:
    def __init__(self):
        self._Empleados= 15
        self._Jefe_de_Departamento = ""

    # Getters y Setters
    def get_empleados(self):
        return self._Empleados

    def set_empleados(self, empleados):
        self._ = empleados

    def get_Jefe_de_Departamento(self):
        return self._Jefe_de_Departamento

    def set_Jefe_de_Departamento(self, Jefe_de_Departamento):
        self._Jefe_de_Departamento = Jefe_de_Departamento

    def mostrar_informacion(self):
        return f"Empleados: {self._Empleados}, JefedeDepartamentos: {self._Jefe_de_Departamento}"