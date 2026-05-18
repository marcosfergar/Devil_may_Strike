#!/bin/sh

echo "Aplicando migraciones en la base de datos de Aiven Cloud..."
flask db upgrade

echo "Iniciando la aplicación en producción con Gunicorn (Puerto 8000)..."
exec gunicorn --bind 0.0.0.0:8000 app.main:app