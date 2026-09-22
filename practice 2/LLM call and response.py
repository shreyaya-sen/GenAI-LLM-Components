import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API key kaha hai meri bhai?")
client = Groq(api_key =my_api_key)
model = "openai/gpt-oss-20b"
role ="user"
prompt = "who created Ai and when was it created?"
#cant write 2 questions making 2 role and prompt as it will only overwrite the previous one so we need to make a list of dicts and then pass it to the model /*
#role = "user"
#prompt = "who is the founder of groq and when was it founded?"
message = [{"role": role, "content":prompt}]
response = client.chat.completions.create(model=model, messages=message)
print("--------------------------------------")
answer = response.choices[0].message.content
print(answer)