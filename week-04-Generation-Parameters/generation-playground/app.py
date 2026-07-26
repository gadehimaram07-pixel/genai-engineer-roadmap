import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def generate(
    prompt,
    temperature=None,
    top_k=None,
    top_p=None,
    max_output_tokens=None,
    presence_penalty=None,
    frequency_penalty=None
):
    try:
        config = {}

        if temperature is not None:
            config["temperature"] = temperature

        if top_k is not None:
            config["top_k"] = top_k

        if top_p is not None:
            config["top_p"] = top_p

        if max_output_tokens is not None:
            config["max_output_tokens"] = max_output_tokens

        if presence_penalty is not None:
            config["presence_penalty"] = presence_penalty

        if frequency_penalty is not None:
            config["frequency_penalty"] = frequency_penalty

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt,
            config=config
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"


print("Gemini Generation Parameter Playground")
while True:
    print("\n1. Generate Response")
    print("2. Compare Temperature")
    print("3. Compare Top-k")
    print("4. Compare Top-p")
    print("5. Compare Max Output Tokens")
    print("6. Compare Presence Penalty")
    print("7. Compare Frequency Penalty")
    print("8. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        print("Generate Response selected.")
        prompt = input("Enter prompt: ")
        print(generate(prompt))

    elif choice == "2":
        print("Temperature Comparison selected.")
        prompt = input("Enter prompt: ")
        print(generate(prompt, temperature=0.1))
        print("=" *50)
        print(generate(prompt, temperature=0.9))
                
    elif choice == "3":
        print("Top-k Comparison selected.")
        prompt = input("Enter prompt: ")
        print(generate(prompt,top_k=1))
        print("=" *50)
        print(generate(prompt,top_k=10))

    elif choice == "4":
        print("Top-p Comparison selected.")
        prompt = input("Enter prompt: ")
        print(generate(prompt,top_p=0.3))
        print("=" *50)
        print(generate(prompt,top_p=0.9))

    elif choice == "5":
        print("Max Output Tokens Comparison selected.")
        prompt = input("Enter prompt: ")
        print(generate(prompt,max_output_tokens=30))
        print("=" *50)
        print(generate(prompt,max_output_tokens=300))

    elif choice == "6":
        print("Presence Penalty Comparison selected.")
        prompt = input("Enter prompt: ")
        print(generate(prompt,presence_penalty=0.0))
        print("=" *50)
        print(generate(prompt,presence_penalty=1.5))

    elif choice == "7":
        print("Frequency Penalty Comparison selected.")
        prompt = input("Enter prompt: ")
        print(generate(prompt,frequency_penalty=0.0))
        print("=" *50)
        print(generate(prompt,frequency_penalty=1.5))

    elif choice == "8":
        print("Thank you for using the playground!")
        break

    else:
        print("Invalid Choice.")