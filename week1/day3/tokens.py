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

#running multiple prompts in a loop
my_prompt1= "Hi!"
my_prompt2 = "Explain time travel in detail under 100 words."
my_prompt3 = "write a 1000 word essay on machine learning"

my_prompts = [my_prompt1, my_prompt2, my_prompt3]

for prompt in my_prompts:
    my_message = {
        "role": my_role,
        "content": prompt
    }

    my_messages = [my_message]

    response = client.chat.completions.create(
        model=my_model,
        messages=my_messages,
        max_tokens=500,)
    
    usage = response.usage

    print(f"Prompt: {prompt} -->your tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total tokens: {usage.total_tokens} Finish Reason: {response.choices[0].finish_reason}")

     

# my_prompt = "Do you know Gaurav Dubey?"

# #message me role and content
# my_message = {
#     "role": my_role,
#     "content": my_prompt
# }

# my_messages = [my_message]

# response = client.chat.completions.create(
#     model=my_model,
#     messages=my_messages)

# print(response)

# print("#"*50)

# answer = response.choices[0].message.content

# print(answer) 

#print("=="*50)

#print(response.usage.total_tokens)

