from database import SessionLocal
from models import Libro

def agregar_libro():
    session = SessionLocal()
    try:
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Género: ")
        estado = input("Estado de lectura: ")

        nuevo = Libro(titulo=titulo, autor=autor, genero=genero, estado=estado)
        session.add(nuevo)
        session.commit()
        print("📚 Libro agregado exitosamente.")
    except Exception as e:
        print("❌ Error al agregar:", e)
    finally:
        session.close()

def listar_libros():
    session = SessionLocal()
    try:
        libros = session.query(Libro).all()
        for libro in libros:
            print(f"{libro.id} - {libro.titulo} ({libro.autor}) [{libro.estado}]")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        session.close()

def buscar_libro():
    session = SessionLocal()
    try:
        termino = input("Buscar por título/autor/género: ")
        resultados = session.query(Libro).filter(
            (Libro.titulo.like(f"%{termino}%")) |
            (Libro.autor.like(f"%{termino}%")) |
            (Libro.genero.like(f"%{termino}%"))
        ).all()

        for libro in resultados:
            print(f"{libro.id} - {libro.titulo} ({libro.autor}) [{libro.estado}]")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        session.close()

def actualizar_libro():
    session = SessionLocal()
    try:
        id_libro = int(input("ID del libro a actualizar: "))
        libro = session.query(Libro).get(id_libro)

        if libro:
            libro.titulo = input("Nuevo título: ") or libro.titulo
            libro.autor = input("Nuevo autor: ") or libro.autor
            libro.genero = input("Nuevo género: ") or libro.genero
            libro.estado = input("Nuevo estado: ") or libro.estado

            session.commit()
            print("✔️ Libro actualizado.")
        else:
            print("❌ No encontrado.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        session.close()

def eliminar_libro():
    session = SessionLocal()
    try:
        id_libro = int(input("ID del libro a eliminar: "))
        libro = session.query(Libro).get(id_libro)

        if libro:
            session.delete(libro)
            session.commit()
            print("🗑️ Libro eliminado.")
        else:
            print("❌ No encontrado.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        session.close()

def menu():
    while True:
        print("\n--- Biblioteca Personal ---")
        print("1. Agregar libro")
        print("2. Listar libros")
        print("3. Buscar libros")
        print("4. Actualizar libro")
        print("5. Eliminar libro")
        print("6. Salir")

        opcion = input("Seleccionar: ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            listar_libros()
        elif opcion == "3":
            buscar_libro()
        elif opcion == "4":
            actualizar_libro()
        elif opcion == "5":
            eliminar_libro()
        elif opcion == "6":
            print("👋 Saliendo...")
            break
        else:
            print("⚠️ Opción inválida")

if __name__ == "__main__":
    menu()
