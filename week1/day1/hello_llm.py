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

my_prompt = "Do you know Gaurav Dubey?"

#message me role and content
my_message = {
    "role": my_role,
    "content": my_prompt
}

my_messages = [my_message]

response = client.chat.completions.create(
    model=my_model,
    messages=my_messages)

print(response)

print("#"*50)

answer = response.choices[0].message.content

print(answer) 

