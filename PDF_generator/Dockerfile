FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libreoffice \
    fonts-liberation \

    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 appuser

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/PDF_generator/

# Передаем права пользователю appuser
RUN chown -R appuser:appuser /app

USER appuser