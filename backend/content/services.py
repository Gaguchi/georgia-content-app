# content/services.py

import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_content(prompt, content_type):
    if content_type == 'social_media':
        instruction = "Write a social media post in Georgian promoting a local business."
    elif content_type == 'blog':
        instruction = "Write a blog post in Georgian about the following topic."
    elif content_type == 'product_description':
        instruction = "Write a product description in Georgian for the following product."
    else:
        instruction = "Generate content in Georgian."

    full_prompt = f"{instruction}\n\n{prompt}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": full_prompt},
        ],
        max_tokens=500,
        temperature=0.7,
    )

    return response['choices'][0]['message']['content'].strip()
