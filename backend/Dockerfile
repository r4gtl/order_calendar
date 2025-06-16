# Dockerfile per Django
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libpq-dev gcc postgresql-client && apt-get clean

WORKDIR /app

COPY backend/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ /app/
COPY backend/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["gunicorn", "order_calendar.wsgi:application", "--bind", "0.0.0.0:8000"]
