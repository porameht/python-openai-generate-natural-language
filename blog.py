import os
import openai
import config

openai.api_key = config.OPENAI_API_KEY

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="Generate blog ideas on: 'casino online'",
  temperature=0.7,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)