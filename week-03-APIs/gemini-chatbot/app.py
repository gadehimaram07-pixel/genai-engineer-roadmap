import os
from dotenv import load_dotenv
from google import genai
import traceback

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
while True:
    prompt = input("USER: ")
    if prompt.lower()=="exit":
        print("Thank You. See you soon again!")
        break
    try:
        response = client.models.generate_content(
            model = "gemini-flash-latest",
            contents = prompt
        )
        print(response.text)
    except Exception as e:
        print(f"Error:{e}")