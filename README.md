# Devil May Strike

[cite_start]Este proyecto es una aplicación web interactiva que integra un videojuego desarrollado en **Unity (WebGL)** con un backend en **Python/Flask**[cite: 9, 10, 11]. [cite_start]Se trata de un *demake* del clásico *Devil May Cry 3* adaptado al género *beat 'em up*[cite: 14, 15].

---

## Guía de Instalación y Ejecución

### 1. Requisitos Previos
* Tener instalado **Python 3.10** o superior.

### 2. Preparar el Entorno Virtual
Abre una terminal en la carpeta del proyecto y ejecuta:
# 1. Crear entorno virtual
Write-Host "Creando entorno virtual .venv"
python -m venv .venv

# 2. Activar el entorno virtual
Write-Host "Activando entorno virtual"
. .\.venv\Scripts\Activate.ps1

# 3. Instalar dependencias
# Test-Path comprueba si existe
if (Test-Path "requirements.txt") {
    Write-Host "Instalando dependencias desde requirements.txt..."
    pip install -r requirements.txt
} else {
    Write-Host "No se encontro requirements.txt. Lea el Readme para mas información"
    return
}

# 4. Ver versiones instaladas
Write-Host "Paquetes instalados:"
pip freeze

# 5. Crea tabals
flask.exe --app app.main crear_tablas

# 5. Ejecutar la aplicación
Write-Host "Ejecutando la aplicación..."
python -m app.main


/DevilMayStrike
│                    
├── /app
│   ├── /clients
│   ├── /database
│   ├── /forms
│   ├── /models
│   ├── /repositories
│   ├── /routes
│   ├── /services
│   ├── /static # CSS, JS e imágenes
│   └── /templates  # Archivos HTML (Jinja2)
│
├── main.py
├── requirements.txt       # Librerías necesarias
└── README.md              # Archivos HTML (Jinja2)
