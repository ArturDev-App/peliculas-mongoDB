import pymongo 

myclient = pymongo.MongoClient('')#Asegurate de colocar tu Host de MongoDB Atlas o Compass
mydb = myclient[''] #Asegurate de ponerle nombre a tu base de datos 
mycol = mydb[""] #Aqui va el nombre de tu coleccion

"""
    Este script solo es una muestra basica de manipulacion de cruw de Peliculas en MongoDB 
    Aegurate de importar la libreria pymongo para tu coneccion de lo contrario el Script no funcionara.
    Utiliza el siguiente comendo desde tu terminal | pip install pymongo 
    Principales Funciones :
     Visualizar \ Agregar \ Editar \ Eliminar \ Buscar 
    
"""

def viewcontent():
    """Mostrar todos los elementos con formato personalizado"""
    peliculas = list(mycol.find())
    if not peliculas:
        print("No hay películas en la base de datos")
        return
    
    print("\n--- TU LISTADO DE PELÍCULAS ---")
    for element in peliculas:
        try:
            # Usar .get() para evitar KeyError si falta el campo
            pelicula = element.get('Pelicula', 'Sin título')
            calificacion = element.get('Calificacion', 'Sin calificación')
            comentarios = element.get('Comentarios', 'Sin comentarios')
            
            # Solo mostrar si tiene título válido
            if pelicula and pelicula != 'Sin título':
                print(pelicula)
                print(calificacion)
                print(f"Comentarios: {comentarios}")
                print()  # Línea en blanco entre películas
            else:
                print(f"⚠️  Documento con datos incompletos: {element}")
                print()
                
        except Exception as e:
            print(f"❌ Error procesando documento: {e}")
            print(f"Documento problemático: {element}")
            print()
        
def formatCalificacion(calificacion):
    """Convertir número a estrellas con espacios"""
    try:
        cal = int(calificacion)
        if 1 <= cal <= 5:
            return " ".join(["★"] * cal)  # Une las estrellas con espacios
        else:
            print("La calificación debe estar entre 1 y 5")
            return "★"
    except ValueError:
        print("La calificación debe ser un número")
        return "★"
        
def addElement(name, calificacion, comentarios):
    """Agregar nueva película"""
    # Verificar si ya existe
    if mycol.find_one({"Pelicula": name}):
        print(f"La película '{name}' ya existe en la base de datos")
        return
    
    # Crear documento (DICCIONARIO, no lista)
    newElement = {
        "Pelicula": name,
        "Calificacion": formatCalificacion(calificacion),
        "Comentarios": comentarios
    }
    
    try:
        mycol.insert_one(newElement)
        print(f"✅ Se ha agregado la película: '{name}' exitosamente")
    except Exception as e:
        print(f"❌ Error al agregar película: {e}")

def editElement(element, correc, promp):
    """Editar elemento existente"""
    if not element:
        print("❌ Escribe un nombre correcto")
        return
    
    # Verificar si existe la película
    pelicula_existente = mycol.find_one({"Pelicula": element})
    if not pelicula_existente:
        print(f"❌ La película '{element}' no se encuentra en la base de datos")
        return
    
    # Preparar la actualización
    update_value = ""
    if correc == "Pelicula":
        update_value = str(promp)
    elif correc == "Calificacion":
        update_value = formatCalificacion(promp)
    elif correc == "Comentarios":
        update_value = str(promp)
    else:
        print("❌ Campo no válido")
        return
    
    try:
        mycol.update_one(
            {"Pelicula": element},
            {"$set": {correc: update_value}}
        )
        print(f"✅ Elemento actualizado correctamente")
    except Exception as e:
        print(f"❌ Error al actualizar: {e}")

def deletElement():
    """Eliminar película"""
    viewcontent()
    pelicula = input("Nombre de la película a eliminar: ")
    
    if not pelicula:
        print("❌ Nombre no válido")
        return
    
    # Verificar si existe
    if not mycol.find_one({"Pelicula": pelicula}):
        print(f"❌ La película '{pelicula}' no existe")
        return
    
    # Confirmar eliminación
    confirmacion = input(f"¿Estás seguro de eliminar '{pelicula}'? (s/n): ")
    if confirmacion.lower() == 's':
        try:
            result = mycol.delete_one({"Pelicula": pelicula})
            if result.deleted_count > 0:
                print(f"✅ Película '{pelicula}' eliminada exitosamente")
            else:
                print("❌ No se pudo eliminar la película")
        except Exception as e:
            print(f"❌ Error al eliminar: {e}")
    else:
        print("Eliminación cancelada")

def searchElement():
    """Buscar película"""
    busqueda = input("Nombre de la película a buscar: ")
    
    if not busqueda:
        print("❌ Ingresa un nombre válido")
        return
    
    # Buscar por nombre exacto o similar
    resultado = mycol.find_one({"Pelicula": {"$regex": busqueda, "$options": "i"}})
    
    if resultado:
        print("\n🔍 PELÍCULA ENCONTRADA:")
        print(f"🎬 {resultado['Pelicula']}")
        print(f"⭐ {resultado.get('Calificacion', 'Sin calificación')}")
        print(f"💭 {resultado.get('Comentarios', 'Sin comentarios')}")
    else:
        print(f"❌ No se encontró ninguna película con '{busqueda}'")

def main():
    print("🎬 BIENVENIDO A TU LISTADO DE PELÍCULAS FAVORITAS 🎬")
    
    menu = True 
    while menu:
        main_menu = """
╔════════════════════════════════════════╗
║        MENÚ PRINCIPAL                  ║
╠════════════════════════════════════════╣
║ 1. Visualizar mi listado              ║
║ 2. Agregar película nueva             ║
║ 3. Editar película                    ║
║ 4. Eliminar película                  ║
║ 5. Buscar película                    ║
║ 6. Salir                              ║
╚════════════════════════════════════════╝
Ingresa tu opción: """
        
        try:
            userOption = input(main_menu).strip()
            
            match userOption:
                case "1":
                    viewcontent()
                    
                case "2":
                    print("\n--- AGREGAR NUEVA PELÍCULA ---")
                    pelicula = input("Nombre de la película: ").strip()
                    if not pelicula:
                        print("❌ El nombre no puede estar vacío")
                        continue
                        
                    calificacion = input("Calificación (1-5): ").strip()
                    comentarios = input("Comentarios: ").strip()
                    addElement(pelicula, calificacion, comentarios)
                    
                case "3":
                    print("\n--- EDITAR PELÍCULA ---")
                    viewcontent()
                    pelicula = input("Nombre de la película a editar: ").strip()
                    
                    if pelicula:
                        campo = input("Campo a editar (Pelicula/Calificacion/Comentarios): ").strip()
                        nuevo_valor = input(f"Nuevo valor para {campo}: ").strip()
                        editElement(pelicula, campo, nuevo_valor)
                    
                case "4":
                    print("\n--- ELIMINAR PELÍCULA ---")
                    deletElement()
                    
                case "5":
                    print("\n--- BUSCAR PELÍCULA ---")
                    searchElement()
                    
                case "6":
                    print("👋 ¡Hasta luego!")
                    menu = False
                    
                case _:
                    print("❌ Opción no válida. Selecciona del 1 al 6")
                    
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            menu = False
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()