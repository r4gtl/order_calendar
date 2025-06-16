#!/bin/bash
set -e

# Se il progetto Django non è ancora stato generato
if [ ! -f "/app/manage.py" ]; then
  echo "📦 Genero progetto Django 'order_calendar'..."
  django-admin startproject order_calendar /app

  cd /app

  echo "🧱 Creo app 'ordini'..."
  python manage.py startapp ordini

  echo "🔐 Correggo permessi (ownership) della cartella /app..."
  chown -R "$(stat -c "%u:%g" /app)" /app
fi

echo "✅ Avvio completato. Eseguo comando finale: $@"
exec "$@"
