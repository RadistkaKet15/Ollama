from ollama_ocr import OCRProcessor
import os

os.environ['OLLAMA_HOST'] = 'http://127.0.0.1:11434'
# Отключаем прокси
os.environ['NO_PROXY'] = '*'
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

# Создаём процессор, указываем модель
ocr = OCRProcessor(model_name='llama3.2-vision:11b')

# Обрабатываем PDF (можно указывать путь к файлу)
result = ocr.process_image(
    image_path="book.pdf",
    format_type="text",  # Можно "text", "markdown", "json" и т.п.
    language="ru"        # Язык распознавания
)

print("Результат OCR:")
print(result)






