FROM python:3.12-slim

# Устанавливаем системные зависимости для OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Python-зависимости
RUN pip install ollama_ocr

# Копируем твой скрипт (замени ollama.py на своё имя, если нужно)
COPY ollama.py /app/ollama.py
# Копируем PDF-файл
COPY book.pdf /app/book.pdf

WORKDIR /app

CMD ["python", "ollama.py"]
