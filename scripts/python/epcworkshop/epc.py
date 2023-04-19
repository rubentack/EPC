import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def run_chatgpt(prompt,wrapper):

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": f"{wrapper} {prompt}"}
  ],
  temperature=1.0,
  n=1
)
return completion.choices[0].message.content


print(completion)