# Devil May Strike 🎮

Una aplicación web interactiva que integra un videojuego desarrollado en **Unity (WebGL)** con un backend robusto en **Python/Flask**. Se trata de un *demake* inspirado en la franquicia Devil May Cry, combinando gameplay envolvente con gestión de usuarios, tienda interactiva y comunidad.

---

## 📋 Descripción del Proyecto

**Devil May Strike** es una plataforma web completa que combina entretenimiento y comunidad. Los usuarios pueden:
- 🎮 Jugar a un videojuego integrado desarrollado en **Unity WebGL**
- 💰 Gestionar su economía de **Orbes Rojos** (divisa del juego)
- 🛍️ Comprar objetos y música en una tienda interactiva
- 🎵 Disfrutar de un reproductor musical persistente
- 💬 Participar en un foro de cazadores con múltiples categorías
- 📚 Explorar la biblioteca de la saga Devil May Cry a través de RAWG API

**Tecnologías principales:**
- Backend: Python 3.10+, Flask, SQLAlchemy
- Frontend: HTML5, CSS3, JavaScript (Vanilla)
- Juego: Unity WebGL
- API: RAWG.io (información de videojuegos)
- Base de Datos: SQLite/PostgreSQL (con Flask-Migrate para migraciones)

---

## 🎯 Funcionalidades Principales

### 🎵 Widget Musical "Persiana"
- **Despliegue Dinámico**: Reproductor integrado en el header que se despliega hacia abajo
- **Inventario Musical**: Solo reproduce pistas compradas previamente en la tienda
- **Persistencia Total**: La música no se corta al navegar; recordará el segundo exacto, canción actual y volumen

### 🏪 Tienda de Objetos y Música
- **Economía de Orbes**: Compra artículos con Orbes Rojos (divisa del juego)
- **Gestión de Inventario**: Productos vinculados a la base de datos del usuario
- **Sincronización en Tiempo Real**: Los cambios se reflejan instantáneamente en el perfil

### 🏛️ Foro de Cazadores
- **Comunidad Interactiva**: Categorías como Taberna, Estrategias y Errores
- **Sistema de Temas**: Hilos de discusión vinculados a perfiles de cazadores
- **Participación Activa**: Comentarios y debates en la comunidad

### 🎮 Integración RAWG API
- **Biblioteca de la Saga**: Información técnica, fechas de lanzamiento y valoraciones
- **Datos en Tiempo Real**: Consulta dinámica de toda la franquicia Devil May Cry

---

## 📦 Requisitos e Instalación

### 1. Requisitos Previos

**Software necesario:**
- **Python 3.10** o superior ([Descargar](https://www.python.org/downloads/))
- **Git** ([Descargar](https://git-scm.com/))
- Una API Key gratuita de [RAWG.io](https://rawg.io/apidocs)

**Verificar instalación:**
```bash
python --version
git --version
```

### 2. Clonar el Repositorio

```bash
git clone https://github.com/marcosfergar/Devil_may_Strike.git
cd Devil_may_Strike
```

### 3. Preparar el Entorno Virtual

**En Windows (PowerShell):**
```powershell
# Crear entorno virtual
python -m venv .venv

# Activar el entorno virtual
.\.venv\Scripts\Activate.ps1

# Si tienes problemas de permisos, ejecuta PowerShell como administrador
```

**En macOS/Linux:**
```bash
# Crear entorno virtual
python3 -m venv .venv

# Activar el entorno virtual
source .venv/bin/activate
```

### 4. Instalar Dependencias

```bash
pip install -r requirements.txt
```

**Dependencias principales:**
- Flask (framework web)
- SQLAlchemy (ORM para base de datos)
- Flask-Migrate (migraciones de BD)
- Requests (llamadas a APIs)
- python-dotenv (manejo de variables de entorno)

---

## ⚙️ Configuración

### 1. Crear Archivo .env

En la raíz del proyecto, crea un archivo `.env` con las siguientes variables:

```env
# RAWG API Configuration
RAWG_API_KEY=tu_api_key_aqui

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True

# Database Configuration
DATABASE_URL=sqlite:///devil_may_strike.db

# Secret Key for Sessions
SECRET_KEY=tu_clave_secreta_aqui
```

**Obtener API Key de RAWG:**
1. Visita [RAWG.io](https://rawg.io/apidocs)
2. Regístrate o inicia sesión
3. Copia tu API Key de la sección de configuración
4. Pégala en el archivo `.env`

### 2. Inicializar la Base de Datos

**Primera ejecución (crear tablas):**
```powershell
flask --app main.py crear_tablas
```

**Desde Linux/macOS:**
```bash
flask --app main.py crear_tablas
```

---

## 🚀 Ejecución en Local

### 1. Activar el Entorno Virtual (si no está activo)

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### 2. Ejecutar la Aplicación

```bash
python main.py
```

**Salida esperada:**
```
 * Serving Flask app 'main'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 3. Acceder a la Aplicación

Abre tu navegador y accede a:
```
http://localhost:5000
```

### 4. Detener la Aplicación

Presiona `Ctrl + C` en la terminal para detener el servidor.

---

## 🔄 Gestión de Base de Datos (Migraciones)

Para evolucionar la base de datos sin perder datos de usuarios (orbes, inventario), usamos **Flask-Migrate**.

### 1. Inicialización (Solo primera vez)

```powershell
flask db init
```

Este comando crea la carpeta `/migrations` necesaria para gestionar cambios.

### 2. Detectar Cambios en Modelos

Después de modificar un modelo en `/app/models`, ejecuta:

```powershell
flask db migrate -m "Descripción del cambio (ej: Añadida columna X a tabla Y)"
```

### 3. Aplicar Cambios a la BD

```powershell
flask db upgrade
```

### 4. Revertir Cambios (si es necesario)

```powershell
flask db downgrade
```

---

## 📂 Estructura del Proyecto

```
Devil_may_Strike/
│
├── /app                          # Paquete principal de la aplicación
│   ├── /database                 # Configuración de SQLAlchemy
│   ├── /models                   # Esquemas de BD (Usuario, Producto, Foro, etc.)
│   ├── /routes                   # Rutas (Home, Tienda, Foro, Perfil, Autenticación)
│   ├── /services                 # Lógica de negocio y consultas
│   ├── /static                   # Archivos estáticos
│   │   ├── /css                  # Estilos CSS
│   │   ├── /js                   # JavaScript (Widget, interacciones)
│   │   ├── /music                # Archivos de música
│   │   ├── /images               # Imágenes y assets
│   │   └── /unity_webgl          # Build de Unity WebGL
│   └── /templates                # Plantillas Jinja2 (HTML)
│       ├── base.html             # Plantilla base
│       ├── home.html
│       ├── shop.html
│       ├── forum.html
│       ├── profile.html
│       └── library.html
│
├── /migrations                   # Migraciones de base de datos (Flask-Migrate)
├── /data                         # Archivos de semilla (productos.json, etc.)
├── main.py                       # Punto de entrada principal
├── requirements.txt              # Dependencias del proyecto
├── .env.example                  # Plantilla de variables de entorno
├── .gitignore                    # Archivos ignorados por Git
└── README.md                     # Esta guía
```

---

## 🐛 Solución de Problemas

### Error: "No module named 'flask'"
**Solución:** Asegúrate de haber activado el entorno virtual y ejecutado `pip install -r requirements.txt`

### Error: "RAWG_API_KEY no configurada"
**Solución:** Verifica que el archivo `.env` existe y contiene la clave API correcta

### La aplicación no inicia en http://localhost:5000
**Solución:** Revisa que el puerto 5000 no esté en uso. Prueba con: `python main.py --port 5001`

### Base de datos corrupta
**Solución:** Elimina `devil_may_strike.db` y ejecuta nuevamente `flask --app main.py crear_tablas`

---

## 📚 Recursos Útiles

- [Documentación Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [RAWG API Documentation](https://rawg.io/apidocs)
- [Unity WebGL Documentation](https://docs.unity3d.com/Manual/WebGL.html)

---

## 👨‍💻 Créditos

**Desarrollador:** Marcos Fernández (@marcosfergar)

**Tecnologías utilizadas:**
- Flask + SQLAlchemy + Flask-Migrate
- JavaScript Vanilla
- Unity WebGL
- RAWG API
- HTML5 + CSS3

**Aviso Legal:** Este es un proyecto educativo. Los derechos de imagen y sonido de Devil May Cry pertenecen a **Capcom**. Este proyecto no tiene fines comerciales.

---

## 📝 Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

**¿Necesitas ayuda?** Abre un [issue](https://github.com/marcosfergar/Devil_may_Strike/issues) en el repositorio.