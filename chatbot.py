import openai
from api_key import api_key

openai.api_key = api_key


messages = []


print("Exit chat with ctrl + c")

while True:
    prompt = input("You: ")
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + f"ChatGpt: {reply}" + "\n")