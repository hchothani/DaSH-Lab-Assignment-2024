import json 
import os
from dotenv import load_dotenv
from groq import Groq
import time

load_dotenv()

client = Groq(
    api_key = os.getenv("API_KEY")
)


with open('input.txt', 'r') as file:
    prompts = file.readlines()

output = []

for prompt in prompts:
    prompt = prompt.strip()
    times = int(time.time())

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assitant.",

            },
            {
               "role": "user",
               "content": prompt, 
            }
        ],
        model="llama3-8b-8192",
    )
    

    timer = int(time.time())

    message = response.choices[0].message.content

    json_output = {
        "Prompt": prompt,
        "Message": message,
        "TimeSent": times,
        "TimeRecvd": timer,
        "Source": "Groq"
    }

    output.append(json_output)

with open('output.json', 'w') as output_file:
    json.dump(output, output_file, indent=4)

print("ouput.json created successfully")
