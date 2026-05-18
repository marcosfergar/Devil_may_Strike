# 1. Bajamos a una versión real y ultra-estable de Python (Slim ocupa muy poco espacio)
FROM python:3.12-slim

# Directorio de trabajo interno del contenedor
WORKDIR /app

# Copiamos los requerimientos instalando Flask y Gunicorn para producción
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && pip install gunicorn

# Copiamos todo el proyecto (incluyendo la carpeta app/ y los archivos de Unity)
COPY . .

RUN mkdir -p data flask_session

# Exponemos el puerto
EXPOSE 8000

# Variables de entorno corregidas apuntando a la carpeta 'app'
ENV FLASK_APP=app/main.py
ENV FLASK_DEBUG=0

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]