class Segip:

    def __init__(self):
        # Inicializar un diccionario vacío para almacenar los nombres y carnet de identidad de los ciudadanos.
        self.citizens = {}

    def add_person(self, name, identification):
        # Verificar si la longitud del carnet de identidad no es igual a 8 dígitos.
        if len(identification) != 8:
            print("Carnet de identidad inválido, debe tener 8 dígitos")
        # Verificar si el carnet de identidad ya existe en el diccionario de ciudadanos.
        elif identification in self.citizens.values():
            print("Carnet de identidad duplicado")
        else:
            # Agregar al ciudadano al diccionario con el nombre como clave y el carnet de identidad como valor.
            self.citizens[name] = identification
            print(f"{name} agregado exitosamente con carnet: {identification}")


# Ejemplo de uso
if __name__ == "__main__":
    print("Bienvenido a SEGIP - Sistema de Registro de Ciudadanos")

    segip = Segip()

    while True:
        print("\nSeleccione una opción:")
        print("1. Agregar un nuevo ciudadano")
        print("2. Ver todos los ciudadanos registrados")
        print("3. Salir")
        choice = input("Ingrese el número de su opción: ")

        if choice == "1":
            name = input("Ingrese el nombre del ciudadano: ")
            identification = input("Ingrese el número de carnet de identidad (8 dígitos): ")
            segip.add_person(name, identification)

        elif choice == "2":
            if not segip.citizens:
                print("Aún no hay ciudadanos registrados.")
            else:
                print("Lista de ciudadanos registrados:")
                for name, identification in segip.citizens.items():
                    print(f"{name}: {identification}")

        elif choice == "3":
            print("Gracias por usar SEGIP - Sistema de Registro de Ciudadanos")
            break

        else:
            print("Opción inválida. Por favor, elija nuevamente.")

