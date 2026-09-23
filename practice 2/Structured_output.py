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
from pydantic import BaseModel
class Ticket(BaseModel):
    name: str
    email: str
    issue: str
json_model_schema = Ticket.model_json_schema()
response_format = {
    "type": "json_object"
}
system_prompt = f"""
extract the personal information from the Ticket strictly based on this schema and returns it in a structured JSON format.
{json_model_schema}
"""
message_system = {"role": "system", "content": system_prompt}
text = "My name is John Doe, my email is john.doe@example.com,i live in delhi I lost my girlfriend her name is radhika and I have an issue with my phone it is not working properly."
prompt = f"""
this is a customer support ticket, extract the personal information from the Ticket strictly based on this schema
{text}"""
message={
    "role": role, "content": prompt
}
messages = [message_system, message]
response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)
answer = response.choices[0].message.content
print(answer)
import json
raw_json = answer
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)
print(ticket.name)
print(ticket.email)
print(ticket.issue)