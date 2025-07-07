from ollama_ocr import OCRProcessor

# Initialize OCR processor
ocr = OCRProcessor(model_name='llama3.2-vision:11b', base_url="http://ollama:11434/api/generate")  # You can use any vision model available on Ollama
# you can pass your custom ollama api

# Process an image
result = ocr.process_image(
    image_path="/app/img.pdf", # path to your pdf files "path/to/your/file.pdf"
    format_type="text",  # Options: markdown, text, json, structured, key_value
    custom_prompt="Extract all text content from this image in English **exactly as it appears**, without modification, summarization, or omission.", # Optional custom prompt
    language="English" # Specify the language of the text (New! 🆕)
)
print(result)