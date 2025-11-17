FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
     PYTHONUNBUFFERED=1 \
     PYTHONPATH=/app \
     APPLICATION_ROOT=/programatransitabilidad

RUN apt-get update && apt-get install -y --no-install-recommends \
     libpq-dev \
     curl \
     && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
