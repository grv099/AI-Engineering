import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

my_model = "llama-3.3-70b-versatile"

my_role = "user"

my_prompt = "Suggest a name for my clothing company."

message_system = {
    "role": "system",
    "content": "You are a brand manager who suggests name for my clothing company. name should be in one word."
}

#message me role and content
my_message = {
    "role": my_role,
    "content": my_prompt
}

my_messages = [message_system, my_message]

# Temperature by default is 0 which means safe. temperature range is 0 to 2. Higher the temperature, more creative the response will be.

response = client.chat.completions.create(
    model=my_model,
    messages=my_messages,
    temperature=0
)

#print(response)

print("#"*50)

answer = response.choices[0].message.content

print(answer)

