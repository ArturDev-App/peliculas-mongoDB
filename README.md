# 🎬 Sistema de Gestión de Películas - MongoDB

Un sistema simple de gestión de películas favoritas usando Python y MongoDB con funcionalidades CRUD completas.

## 📋 Características

- ✅ **Visualizar** listado de películas
- ✅ **Agregar** nuevas películas con calificación por estrellas
- ✅ **Editar** información de películas existentes
- ✅ **Eliminar** películas del listado
- ✅ **Buscar** películas por nombre
- ✅ Sistema de calificación visual con estrellas (★)
- ✅ Interfaz de usuario intuitiva por consola

## 🛠️ Tecnologías

- **Python 3.x**
- **MongoDB** (local o Atlas)
- **PyMongo** - Driver de MongoDB para Python

## 📦 Instalación

### Prerrequisitos

1. **Python 3.x** instalado
2. **MongoDB** (local) o cuenta en **MongoDB Atlas**
3. **MongoDB Compass** (opcional, para visualización gráfica)

### Pasos de instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/peliculas-mongodb.git
   cd peliculas-mongodb
   ```

2. **Instala las dependencias:**
   ```bash
   pip install pymongo
   ```

3. **Configura la conexión a MongoDB:**
   
   Edita las líneas 3-5 del archivo `peliculas_app.py`:
   
   ```python
   # Para MongoDB local:
   myclient = pymongo.MongoClient('mongodb://localhost:27017/')
   
   # Para MongoDB Atlas:
   myclient = pymongo.MongoClient('mongodb+srv://usuario:password@cluster.mongodb.net/')
   
   mydb = myclient['mi_base_de_datos']  # Nombre de tu base de datos
   mycol = mydb["peliculas"]            # Nombre de tu colección
   ```

## 🚀 Uso

1. **Ejecuta la aplicación:**
   ```bash
   python peliculas_app.py
   ```

2. **Navega por el menú:**
   ```
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
   ```

## 📊 Estructura de Datos

Cada película se almacena como un documento JSON:

```json
{
  "_id": "ObjectId",
  "Pelicula": "Nombre de la película",
  "Calificacion": "★ ★ ★ ★ ★",
  "Comentarios": "Tus comentarios sobre la película"
}
```

## 🔧 Funcionalidades

### Agregar Película
- Nombre de la película
- Calificación del 1 al 5 (se convierte automáticamente a estrellas)
- Comentarios personales

### Visualizar Listado
```
--- TU LISTADO DE PELÍCULAS ---

Spiderman
★ ★ ★ ★ ★
Comentarios: Excelente película de superhéroes

The Matrix
★ ★ ★ ★
Comentarios: Película de ciencia ficción increíble
```

### Buscar Películas
- Búsqueda por nombre (no sensible a mayúsculas/minúsculas)
- Usa expresiones regulares para búsquedas parciales

### Editar Películas
- Modificar nombre, calificación o comentarios
- Validación de datos de entrada

### Eliminar Películas
- Confirmación antes de eliminar
- Eliminación segura con verificación

## 🛡️ Manejo de Errores

- Validación de conexión a MongoDB
- Manejo de documentos duplicados
- Validación de entrada de usuario
- Manejo de excepciones graceful

## 📝 Comandos MongoDB Útiles

```javascript
// Ver todas las bases de datos
show dbs

// Usar base de datos
use mi_base_de_datos

// Ver todas las películas
db.peliculas.find()

// Buscar película específica
db.peliculas.find({"Pelicula": "Spiderman"})

// Contar películas
db.peliculas.count()
```

## 🤝 Contribuciones

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Tu Nombre** - [@ArturDev-App](https://github.com/ArturDev-App)

## 🔮 Futuras Mejoras

- [ ] Interfaz web con Flask/Django
- [ ] Sistema de géneros de películas
- [ ] Exportar listado a CSV/PDF
- [ ] Sistema de recomendaciones
- [ ] Interfaz gráfica con Tkinter
- [ ] API REST
- [ ] Autenticación de usuarios
- [ ] Subida de imágenes de películas

---

⭐ **¡Si te gusta este proyecto, dale una estrella!** ⭐
