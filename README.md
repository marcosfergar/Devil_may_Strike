# Devil May Strike

Este proyecto es una aplicación web interactiva que integra un videojuego desarrollado en **Unity (WebGL)** con un backend robusto en **Python/Flask**. Se trata de un *demake* inspirado en el universo de *Devil May Cry*, fusionando mecánicas de *beat 'em up* con un ecosistema web completo para el jugador.

---

## Funcionalidades Principales

### 🎵 Widget Musical "Persiana"
* **Despliegue Dinámico**: Reproductor integrado en el header que se despliega hacia abajo al pulsar el icono del disco.
* **Inventario Musical**: Solo reproduce las pistas que el usuario ha comprado previamente en la tienda.
* **Persistencia Total**: La música no se corta al navegar entre páginas; el sistema recuerda el segundo exacto, la canción actual y el volumen mediante `localStorage`.

### 🏪 Tienda de Objetos y Música
* **Economía de Orbes**: Compra de artículos utilizando *Orbes Rojos* (divisa del juego).
* **Gestión de Inventario**: Los productos se vinculan a la base de datos del usuario (`SQLAlchemy`) y se reflejan instantáneamente en el perfil.

### 🏛️ Foro de Cazadores
* **Comunidad Interactiva**: Diferentes categorías (Taberna, Estrategias, Errores) para que los usuarios interactúen.
* **Hilos de Discusión**: Sistema completo de temas y mensajes vinculados a cada perfil de cazador.

### 🎮 Integración con RAWG API
* **Biblioteca de la Saga**: Consulta de información técnica, fechas de lanzamiento y valoraciones de toda la franquicia *Devil May Cry* en tiempo real.

---

## 🛠️ Guía de Instalación y Ejecución

### 1. Requisitos Previos
* **Python 3.10** o superior.
* Una API Key de [RAWG.io](https://rawg.io/apidocs).

### 2. Preparar el Entorno (PowerShell)
```powershell
# 1. Crear entorno virtual
python -m venv .venv

# 2. Activar el entorno virtual
.\.venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
# Crea un archivo .env o establece las variables:
$env:RAWG_API_KEY = "tu_api_key_aqui"
```

### 3. Inicializar la Base de Datos
```powershell
flask --app main.py crear_tablas
```

### 4. Ejecutar la Aplicación
```powershell
python main.py
```

### 📂 Estructura del Proyecto
```powershell
/DevilMayStrike
│
├── /app
│   ├── /database      # Conexión y configuración de SQLAlchemy
│   ├── /models        # Esquemas de DB (Usuario, Producto, Foro)
│   ├── /routes        # Lógica de rutas (Home, Tienda, Foro, Perfil)
│   ├── /services      # Lógica de negocio (Consultas a DB y RAWG API)
│   ├── /static        # CSS, JS (Widget), Música, Imágenes y Unity WebGL
│   └── /templates     # Plantillas Jinja2 (plantilla_base.html, home.html, etc.)
│
├── /data              # Archivos de semilla (productos.json)
├── main.py            # Punto de entrada y comandos CLI
├── requirements.txt   # Librerías necesarias
└── README.md          # Esta guía
```
### Créditos y Notas
Desarrollador: Marcos Fernández.

Tecnologías: Flask, SQLAlchemy, JavaScript (Vanilla), Unity WebGL.

Aviso Legal: Este es un proyecto educativo. Los derechos de imagen y sonido de Devil May Cry pertenecen a Capcom.