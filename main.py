from classEmpleado import Empleado
from classDepartamento import Departamento
from classArea import Area
from classDirector import Director
from classGerente import Gerente
from classJefeArea import JefeArea

def main():
    # Crear instancias de las clases
    empleado = Empleado()
    empleado.set_nombre("Dayren")
    empleado.set_apellido("Morales")
    empleado.set_edad(25)
    empleado.set_cargo("SubDirector")
    empleado.set_tipo_contrato("Temporal")

    departamento = Departamento()
    departamento.set_empleados(15)
    departamento.set_Jefe_de_Departamento("Oficina 5")

    area = Area()
    area.set_descripcion("Edificio Y")
    area.set_departamentos(8)

    director = Director()
    director.set_contratacion("Temporal")
    director.set_salario(3500)

    gerente = Gerente()
    gerente.set_telefono(5612603647)
    gerente.set_nivel_gerencial("Gerencia Media")

    jefearea = JefeArea()
    jefearea.set_supervisados(4)
    jefearea.set_nivel_jerarquico(5)

    # Mostrar la información
    print("Empleado")
    print(empleado.mostrar_informacion())

    print("Departamento")
    print(departamento.mostrar_informacion())

    print("Area")
    print(area.mostrar_informacion())

    print("Director:")
    print(director.mostrar_informacion())

    print("Gerente:")
    print(gerente.mostrar_informacion())

    print("Jefe de Área:")
    print(jefearea.mostrar_informacion())

if __name__ == "__main__":
    main()



