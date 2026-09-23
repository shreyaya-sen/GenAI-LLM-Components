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
prompt1 = "who created Ai and when was it created?"
prompt2 = "explain the history of Ai in detail in 500 words"
prompt3 = "explain the history of india in 1000 words"
prompts = [prompt1, prompt2, prompt3]
for prompt in prompts:
    message = [{"role": role, "content": prompt}]
    response = client.chat.completions.create(model=model, messages=message, max_tokens=3000)
    usage = response.usage
    print(f"Prompt: {prompt} --> your token usage is: {usage.prompt_tokens} completion tokens: {usage.completion_tokens} total tokens: {usage.total_tokens}")
    print(f"Finish Reason: {response.choices[0].finish_reason}")