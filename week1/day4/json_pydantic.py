import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

class TicketSchema(BaseModel):
    name: str
    email: str
    phone: str
    address: str

schema = TicketSchema.model_json_schema()

my_response_format = {
    "type": "json_object"
}


my_model = "llama-3.3-70b-versatile"

my_role = "user"

my_system_prompt = f''' return output in json format matching this schema: {schema} '''


my_system_message = {
    "role": "system",
    "content": my_system_prompt
}

text="Hello My name is Pratyush.Yesterday I broke up with my girlfriend sheetal. I have an iphone which is not working at all. My address is delhi. My email is abc@gmail.com. My contact number is 82134"

#ftype string used to extract the data from the text. You can use any of the following types: email, phone, address, name, date, time, url, ip_address, credit_card, ssn, vehicle_number, passport_number, bank_account_number
my_prompt = f''' This is a customer ticket. Please extract the personal information from this: {text}'''

#message me role and content
my_message = {
    "role": my_role,
    "content": my_prompt
}

my_messages = [my_system_message,my_message]

response = client.chat.completions.create(
    model=my_model,
    messages=my_messages,
    temperature=0,
    response_format=my_response_format)

# print(response)

# print("#"*50)

answer = response.choices[0].message.content

print(answer) 

#isko code kaise padega
import json
raw_json=answer
#making data file
data_file = json.loads(raw_json)
ticket = TicketSchema(**data_file)

#inko pass kr skte hai aage
print(ticket.name)
print(ticket.email)
print(ticket.phone)
print(ticket.address)

