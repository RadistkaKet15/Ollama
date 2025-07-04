import os
import base64
import io
import requests
import json
from pdf2image import convert_from_path

# Отключаем прокси
os.environ['NO_PROXY'] = '*'
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

# 📄 Конвертируем первую страницу PDF в PIL.Image
pages = convert_from_path('C:/Users/Home/PycharmProjects/Ollama/book.pdf', dpi=300)
img = pages[0]

# 🖼️ Конвертируем изображение в base64
buffered = io.BytesIO()
img.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# 📡 Формируем запрос к Ollama
url = "http://localhost:11438/api/generate"
headers = {"Content-Type": "application/json"}
payload = {
    "model": "llama3.2-vision:11b",
    #"prompt": "Extract all visible text from this pdf img.pdf file in ru without any changes",
    "image": img_str
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    # 🧾 Ответ приходит в формате NDJSON — одна JSON-строка на строку
    result_text = ""
    for line in response.content.splitlines():
        line = line.strip()
        if line:
            obj = json.loads(line)
            if "response" in obj:
                result_text += obj["response"]
    print("Результат:")
    print(result_text.strip())
else:
    print("Ошибка:", response.status_code, response.text)
