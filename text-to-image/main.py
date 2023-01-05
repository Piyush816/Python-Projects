import os
import openai


# Load your API key from an environment variable or secret management service
openai.api_key = "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"

prompt = input("Enter prompt: ")

response = openai.Image.create(
  prompt=prompt,
  n=1,
  size="512x512"
)
image_url = response['data'][0]['url']

print(image_url)