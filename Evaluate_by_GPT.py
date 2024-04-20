# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 20:37:51 2024

@author: 10364
"""

import openai            # pip install openai==0.28.1

openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# prompt
content =  "Question: What is lumina strawberry?ChatGPT-3.5: As of my last update in January 2022, there isn't a specific variety of strawberry called Lumina that I'm aware of. It's possible that it could be a newer variety developed or introduced after that time. LLaMA-7B: Thank you for asking! I'm here to help you with any questions you may have. However, I must inform you that lumina strawberry is not a real or valid term. It is possible that you may have misspelled the name of a strawberry variety or that it is a fictional term. ChatAgronomist: Lumina strawberry is a new cultivar developed by the USDA-ARS breeding program. It produces large, sweet, and bright red strawberries with a glossy appearance and creamy texture. Notably, it's resistant to foliar diseases like anthracnose fruit rot and has an excellent shelf life. Lumina strawberries debut earlier in the season, typically in late April to early May, compared to other varieties in the Mid-Atlantic region."
print("content:  " + content)
prompt1 = "Please evaluate and rate the responses to Questions for the following three models, ChatAgronomist, ChatGPT-3.5, and LLaMA-7B, with a range of 0-5. The higher the score, the more accurate the answer. \n"
prompt2= "Responses: {" + content + "}"

prompt_final = prompt1 + prompt2 

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt_final}
  ]
)

print("----------------------------------------------")
print("Result: \n", completion.choices[0].message.content)