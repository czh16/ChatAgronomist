# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:00:15 2024

@author: 10364
"""

import openai            # pip install openai==0.28.1
import pinecone          # pip install pinecone-client==2.2.4
                         # pip install --upgrade urllib3

openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxx"
pinecone.init(api_key="xxxxxxxxxxxxxxxxxxxxxx", environment="gcp-starter")

# prompt
prompt = "I'm planning to start planting strawberries on my farm and I've heard that botrytis gray mold is a common problem. The weather here usually ranges between 65-75°F, especially during the bloom period, and we get quite a bit of rainfall. I'm looking for both conventional and organic ways to prevent and treat this disease. What would you recommend?"

# connect to the the db
index = pinecone.Index("czh")
print("****************** Initialize： Done ******************")

promt_embedding_res = openai.Embedding.create(
    model="text-embedding-ada-002",
    input = prompt
)
print("****************** Generate embedding vector： Done ******************")

prompt_res = index.query(
    promt_embedding_res['data'][0]['embedding'],
    top_k = 5,
    include_metadata = True
)
print("****************** Retrieve information： Done ******************")

contexts = [item['metadata']['text'] for item in prompt_res['matches']]
prompt_final = prompt + "The following are materials:"+"\n\n---\n\n".join(contexts)+"\n\n-----\n\n"
print("prompt_final:  " + prompt_final)
print("****************** Reconstruct prompts： Done ******************")

# communicate with LLM
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt_final}
  ]
)

print("User: ", prompt)
print("AI: ", completion.choices[0].message.content)