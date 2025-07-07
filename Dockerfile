FROM python:3.12-slim

# Устанавливаем системные зависимости (включая libgl1 для OpenCV)
RUN apt-get update && \
    apt-get install -y \
        poppler-utils \
        tesseract-ocr \
        libgl1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "test.py"]