# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 20:19:48 2024

@author: 10364
"""

import openai            # pip install openai==0.28.1

openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# prompt
content = "Based on some studies the optimal temperature for strawberry plant growth is 15–26°C . During flowering stage, it’s best to maintain a temperature range of 16-20°C. However, once the plants bear fruit, a range of 15-16°C is ideal for maturation. However, this temperature varies among different cultivars. Strawberry cultivars exhibit two primary categories based on their flowering patterns: seasonal flowering, commonly known as June-bearing, and perpetual flowering, also referred to as everbearing. In the case of June-bearing strawberries, flowering is triggered by the combination of short-day conditions and low temperatures in autumn. Following this initiation, the plant enters a dormant phase throughout the winter, culminating in a singular harvest season during the summer. On the other hand, everbearing strawberries possess the flexibility to initiate flowering under various photoperiods and within a moderate temperature range. This adaptability results in an extended harvest season, spanning from spring through to autumn."

print("content:  " + content)
prompt1 = "Extract a virtual conversation about strawberry planting from the Knowledge, and hypothesize a famer is consulting a strawberry agronomist about relevant planting knowledge and information. \n"
prompt2 = "Use the following JSON format as output: \n"
prompt3 = "[\n"
prompt4 = "{instruction: \" If you are an agronomist, please answer the farmer questions based on the farmer's description.\",\n"
prompt5 = "input: farmer's description,\n"
prompt6 = "output: agronomist’s response}\n"
prompt7 = "]\n"
prompt8 = "The extracted result should exclude words triggering OpenAI content management policy.\n"
prompt9 = "\n"
prompt10 = "Knowledge: {" + content + "}"

prompt_final = prompt1 + prompt2 + prompt3 + prompt4 + prompt5 + prompt6 + prompt7 + prompt8 + prompt9 + prompt10

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt_final}
  ]
)

print("----------------------------------------------")
print("Result: \n", completion.choices[0].message.content)