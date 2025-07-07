<h1 align="center">Ollama OCR</h1>
A powerful OCR (Optical Character Recognition) package that uses state-of-the-art vision language models through Ollama to extract text from images and PDF.
# Ollama OCR Processor

Проект для извлечения текста из PDF-файлов с помощью моделей компьютерного зрения Ollama (например, `granite3.2-vision`). Результат сохраняется в форматах `markdown`, `text`, `json` и др.

## 🛠 Технологии
- **Ollama** (для запуска моделей ИИ)
- **Python 3.12**
- **pdf2image** (конвертация PDF в изображения)
- **Docker** (изоляция окружения)

## ⚙️ Установка

### 1. Клонирование репозитория
```bash
git clone https://github.com/RadistkaKet15/Ollama.git
cd Ollama
```
### 2. Запуск через Docker Compose
``` bash
docker-compose up --build
```
## 🚀 Использование

Основные параметры в test.py:
```bash
python
ocr = OCRProcessor(
    model_name='granite3.2-vision',  # Любая vision-модель Ollama
    base_url="http://ollama:11434/api/generate",
    language="Russian",              # Язык текста
    format_type="markdown"          # Формат вывода
)

```

## 📌 Настройка
1. **Модель**: Замените granite3.2-vision на нужную модель (предварительно скачайте через ollama pull).
    #### Модели:
    ```
    ollama pull llama3.2-vision:11b
    ollama pull granite3.2-vision
    ollama pull moondream
    ollama pull minicpm-v
    ```
2. **PDF-файлы**: Положите файлы в папку /app или измените путь в image_path.

3. **Формат вывода**: Доступны варианты: markdown, text, json, structured, key_value.

## 🐳 Docker-особенности
- Для GPU раскомментируйте секцию deploy в docker-compose.yml.

- Ollama автоматически скачивает модели при первом запуске (может занять время).

## 📂 Структура проекта
```
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── test.py                # Основной скрипт обработки
```
## 🔧 Пример вывода
Результат сохраняется в **/app/ocr_result.txt**:
```
# Пример извлечённого текста
Это текст из вашего PDF...
```
## Выходные примеры:
