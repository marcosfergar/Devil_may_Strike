FROM python:3.14.3
# directorio trabajo
WORKDIR /app

# dependencias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# librerias
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000

# Variables de entorno para Flask
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

CMD ["flask", "run"]