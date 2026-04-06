# Devil May Strike

[cite_start]Este proyecto es una aplicación web interactiva que integra un videojuego desarrollado en **Unity (WebGL)** con un backend en **Python/Flask**[cite: 9, 10, 11]. [cite_start]Se trata de un *demake* del clásico *Devil May Cry 3* adaptado al género *beat 'em up*[cite: 14, 15].

---

## Guía de Instalación y Ejecución

### 1. Requisitos Previos
* Tener instalado **Python 3.10** o superior.

### 2. Preparar el Entorno Virtual
Abre una terminal en la carpeta del proyecto y ejecuta:

python -m venv .venv

.\venv\Scripts\pip.exe install flask

pip install -r requirements.txt

# Crear el entorno
python -m venv venv


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