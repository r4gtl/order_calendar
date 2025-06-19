#!/bin/bash
set -e

# 🔐 Correggi i permessi all'avvio basandoti sull'owner dell'host (dinamico)
APP_OWNER_UID=$(stat -c '%u' /app)
APP_OWNER_GID=$(stat -c '%g' /app)

echo "🔐 Correggo permessi per UID:$APP_OWNER_UID GID:$APP_OWNER_GID"
chown -R "$APP_OWNER_UID:$APP_OWNER_GID" /app


# Se il progetto Django non è ancora stato generato
if [ ! -f "/app/manage.py" ]; then
  echo "📦 Genero progetto Django 'order_calendar'..."
  django-admin startproject order_calendar /app

  cd /app

  echo "🧱 Creo app 'ordini'..."
  python manage.py startapp ordini

  #echo "🔐 Correggo permessi (ownership) della cartella /app..."
  #chown -R "$(stat -c "%u:%g" /app)" /app
fi
echo "🔐 Rendo scrivibile a tutti la cartella /app"
chmod -R 777 /app


echo "✅ Avvio completato. Eseguo comando finale: $@"
exec "$@"
