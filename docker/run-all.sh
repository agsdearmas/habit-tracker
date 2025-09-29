#!/bin/bash

echo "> Iniciando servicios con Docker Compose..."

# Reconstrir la imagen de la app si hay cambios en el codigo/Dockerfile
docker-compose up -d --build

echo "> Servicios iniciados. Verificando logs (Ctrl+C para salir de los logs, los contenedores seguiran activos)..."

# Mostrar logs combinados de ambos servicios, sin detiene la ejecucion del script
docker-compose logs -f