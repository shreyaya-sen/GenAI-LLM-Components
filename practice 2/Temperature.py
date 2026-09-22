import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
my_api_key =os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API key kaha hai meri bhai?")
client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-20b"
role = "user"
prompt = "suggest me a clothing brand name for my new clothing brand"
message = [{"role": role, "content": prompt}]
#response = client.chat.completions.create(model=model, messages=message, temperature=2)    
response = client.chat.completions.create(model=model, messages=message,temperature=1) 
print("--------------------------------------")
answer = response.choices[0].message.content
print(answer)