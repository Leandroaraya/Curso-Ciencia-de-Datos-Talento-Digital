# main.py

from src.gestor import GestorContactos
from src.contacto import Contacto

# Inicializamos el gestor
gestor = GestorContactos()

def menu():
    print("\n=== Bienvenido al Gestor de Contactos ===")
    print("1 - Ver contactos")
    print("2 - Agregar un nuevo contacto")
    print("3 - Eliminar un contacto")
    print("4 - Editar un contacto")
    print("5 - Buscar por nombre o teléfono")
    print("0 - Salir")
    return input("Seleccione una opción: ")

while True:
    opcion = menu()

    if opcion == "1":
        print("\n--- Lista de Contactos ---")
        gestor.listar_contactos()

    elif opcion == "2":
        print("\n--- Agregar Contacto ---")
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        direccion = input("Dirección: ")
        c = Contacto(nombre, telefono, correo, direccion)
        gestor.agregar_contacto(c)
        if gestor.agregar_contacto(c):
            print("✅ Contacto agregado.")
        else:
            print("❌ No se pudo agregar el contacto por duplicado.")

    elif opcion == "3":
        print("\n--- Eliminar Contacto ---")
        texto = input("Ingrese nombre o teléfono del contacto a eliminar: ")
        encontrados = gestor.buscar_contacto(texto)
        if encontrados:
            for idx, c in enumerate(encontrados, 1):
                print(f"{idx} - {c}")
            eleccion = input("Ingrese el número del contacto a eliminar: ")
            try:
                seleccionado = encontrados[int(eleccion)-1]
                gestor.eliminar_contacto(seleccionado)
                print("✅ Contacto eliminado.")
            except (ValueError, IndexError):
                print("Opción inválida.")
        else:
            print("❌ No se encontró ningún contacto.")

    elif opcion == "4":
        print("\n--- Editar Contacto ---")
        texto = input("Ingrese nombre o teléfono del contacto a editar: ")
        encontrados = gestor.buscar_contacto(texto)
        if encontrados:
            for idx, c in enumerate(encontrados, 1):
                print(f"{idx} - {c}")
            eleccion = input("Ingrese el número del contacto a editar: ")
            try:
                c = encontrados[int(eleccion)-1]
                print(f"Editando contacto: {c}")
                nuevo_nombre = input("Nuevo nombre (Enter para mantener): ")
                nuevo_telefono = input("Nuevo teléfono (Enter para mantener): ")
                nuevo_correo = input("Nuevo correo (Enter para mantener): ")
                nueva_direccion = input("Nueva dirección (Enter para mantener): ")
                c.actualizar(
                    nombre=nuevo_nombre or None,
                    telefono=nuevo_telefono or None,
                    correo=nuevo_correo or None,
                    direccion=nueva_direccion or None
                )
                gestor.guardar_contactos()
                print("✅ Contacto actualizado.")
            except (ValueError, IndexError):
                print("Opción inválida.")
        else:
            print("❌ No se encontró ningún contacto.")

    elif opcion == "5":
        print("\n--- Buscar Contacto ---")
        texto = input("Ingrese nombre o teléfono: ")
        resultados = gestor.buscar_contacto(texto)
        if resultados:
            print(f"Se encontraron {len(resultados)} contacto(s):")
            for r in resultados:
                print(r)
        else:
            print("❌ No se encontró ningún contacto.")

    elif opcion == "0":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida, intente nuevamente.")
