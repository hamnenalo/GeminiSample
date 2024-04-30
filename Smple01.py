import os
import google.generativeai as genai

# Setting API-Key
API_KEY=os.getenv('API_Key')
genai.configure(api_key=API_KEY)

gemini_pro = genai.GenerativeModel("gemini-pro")
prompt = "Hello!"
response = gemini_pro.generate_content(prompt)

print(response.text)

