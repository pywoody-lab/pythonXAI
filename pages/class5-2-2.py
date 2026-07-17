import openai as ai#pip install openai
from dotenv import load_dotenv
import os
load_dotenv()#載入.env檔案內容
#設定API金鑰
ai.api_key=os.getenv('OPENAI_API_KEY')
messages=[{"role": "system", "content": "請用繁體中文進行後續對話"},]
while True:
    user_input=input("你：") 
    if user_input.lower() in ['exit','quit']:
        break
    messages.append({"role": "user", "content": user_input})
    response=ai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        )
    assistant_response=response.choices[0].message.content
    print("AI：",assistant_response)
    messages.append({"role": "assistant", "content": assistant_response})
