from ollama_ocr import OCRProcessor
import time

start = time.time()
# Initialize OCR processor
ocr = OCRProcessor(model_name='granite3.2-vision', base_url="http://ollama:11434/api/generate")  # You can use any vision model available on Ollama
# you can pass your custom ollama api

# Process an image
result = ocr.process_image(
    image_path="/app/img.pdf", # path to your pdf files "path/to/your/file.pdf"
    format_type="markdown",  # Options: markdown, text, json, structured, key_value
    #custom_prompt="Распознай текст максимально точно, сохраняя сходное форматирование. Не изменяй и не перефразируй текст - просто извлеки его в том виде, в котором он представлен", # Optional custom prompt
    language="Russian" # Specify the language of the text (New! )
)
print(result)

# Save result to a file
output_file_path = "/app/ocr_result.txt"  # Укажите желаемый путь для сохранения файла
try:
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(result)
    print(f"Результат успешно сохранён в файл: {output_file_path}")
except Exception as e:
    print(f"Ошибка при сохранении файла: {e}")
print(f"Time: {time.time() - start}")