## Version web: https://gestor-contactos-app-9rqgqdi8o2uapz9h9pxvu6.streamlit.app/

# 📇 Gestor de Contactos en Python

Este proyecto corresponde al desarrollo de un **Gestor de Contactos** implementado en Python como parte de una actividad académica del curso.  
El objetivo principal fue aplicar conceptos fundamentales del lenguaje Python mediante la creación de una aplicación funcional, modular y persistente.

La aplicación permite **gestionar contactos personales**, ofreciendo operaciones completas de creación, lectura, actualización y eliminación (CRUD), junto con almacenamiento persistente de los datos.

---

## 🧩 Descripción de la actividad

La actividad consistió en diseñar e implementar un sistema capaz de administrar una lista de contactos, simulando un caso real de gestión de información personal.  
Para ello, se abordaron las siguientes etapas:

1. **Modelado de la información**
   - Definición de una clase `Contacto` que representa a cada persona.
   - Cada contacto contiene nombre, teléfono, correo electrónico y dirección.

2. **Gestión de datos**
   - Implementación de una clase `GestorContactos` encargada de administrar la colección de contactos.
   - Validación de datos obligatorios (nombre y teléfono).
   - Prevención de contactos duplicados.
   - Búsqueda flexible por nombre o teléfono.

3. **Persistencia de la información**
   - Uso de un archivo **JSON** para guardar los contactos.
   - Carga automática de los registros al iniciar la aplicación.
   - Guardado automático de los cambios al agregar, editar o eliminar contactos.
   - Esto permite mantener continuidad de los datos entre ejecuciones del programa.

4. **Separación de responsabilidades**
   - La lógica de negocio se mantiene en la carpeta `src`.
   - Las interfaces (terminal y web) consumen la misma lógica.
   - Se evita la duplicación de código y se facilita el mantenimiento.

---

## 🖥️ Modos de ejecución

El proyecto ofrece **dos interfaces de uso**, ambas basadas en la misma lógica interna:

### 🔹 Versión en terminal (`main.py`)
Permite interactuar con el gestor mediante un menú textual en la consola, ideal para comprender el flujo lógico del programa y reforzar el uso de estructuras de control como condicionales y bucles.

Ejecución:

python main.py


### 🔹 Versión web  (`app.py`)
Desarrollada utilizando Streamlit, esta versión proporciona una interfaz gráfica accesible desde el navegador.
Facilita la visualización de contactos y mejora la experiencia de usuario, permitiendo interactuar mediante formularios, botones y listas desplegables.

Ejecución local:

streamlit run app.py
