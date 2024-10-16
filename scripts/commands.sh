#!/bin/sh
set -e  # Interrompe o script se ocorrer um erro

# Espera pelo banco de dados PostgreSQL estar disponível
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    echo "Waiting for PostgreSQL to start at $POSTGRES_HOST:$POSTGRES_PORT..."
    sleep 2
done

echo "PostgreSQL started successfully at $POSTGRES_HOST:$POSTGRES_PORT"

# Coleta arquivos estáticos
#echo "Collecting static files..."
#python manage.py collectstatic --noinput

# Aplica migrações
echo "Applying database migrations..."
python manage.py migrate --noinput

# Inicia o servidor Django
echo "Starting Django server on 0.0.0.0:8081"
python manage.py runserver 0.0.0.0:8081
