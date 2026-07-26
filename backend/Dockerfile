FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install LibreOffice and tools needed for conversions
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       libreoffice \
       libreoffice-writer \
       libreoffice-core \
       poppler-utils \
       unzip \
       build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install (filter out windows-only packages like pywin32)
COPY requirements.txt /app/requirements.txt
RUN sed '/pywin32/d' /app/requirements.txt > /app/requirements-linux.txt \
    && pip install --no-cache-dir -r /app/requirements-linux.txt

# Copy project
COPY . /app

WORKDIR /app

EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
