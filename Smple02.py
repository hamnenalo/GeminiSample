import os
import google.generativeai as genai

# Setting API-Key
API_KEY=os.getenv('API_Key')
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")
# Initializ history
chat = model.start_chat(history=[])

print("question please. 'exit' is end")

while True:
    # Input
    user_input = input("Input question : ")

    # Exit
    if user_input == "exit":
        print("Thank! finished")
        break
    
    # Response
    response = chat.send_message(user_input)
    print(response.text)