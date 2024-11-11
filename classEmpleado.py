from classPersona import Persona

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self._cargo = ""
        self._tipo_contrato = ""

    # Getters y Setters
    def get_cargo(self):
        return self._cargo

    def set_cargo(self, cargo):
        self._cargo = cargo

    def get_tipo_contrato(self):
        return self._tipo_contrato

    def set_tipo_contrato(self, tipo_contrato):
        self._tipo_contrato = tipo_contrato

    def mostrar_informacion(self):
        persona_info = super().mostrar_informacion()
        return (f"Empleado: Nombre: {self._nombre}, Apellido: {self._apellido}, Edad: {self._edad}, "
                f"cargo: {self._cargo}, tipo_contrato: {self._tipo_contrato},")