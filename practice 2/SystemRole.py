import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API key kaha hai meri bhai?")
client= (Groq(api_key=my_api_key))
model = "openai/gpt-oss-20b"
role= "user"
prompt= "i am deeply in love with you"
#message_system = {"role": "system", "content": "you are my boyfriend"}
message_system = {"role": "system", "content": "you are my strict manager and you will not let me do anything that is not work related and you will scold me if i do anything that is not work related"}
message = {"role":role, "content": prompt}
messages = [message_system, message]
response =client.chat.completions.create(model=model,messages=messages)
print("--------------------------------------")
answer = response.choices[0].message.content
print(answer)