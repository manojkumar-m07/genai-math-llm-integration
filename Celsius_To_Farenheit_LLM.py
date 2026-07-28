#!/usr/bin/env python
# coding: utf-8

# In[28]:


import os
import json
import openai
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# In[29]:


# Function to convert Celsius to Fahrenheit
def convert_c_to_f(celsius):
    fahrenheit = (float(celsius) * 9/5) + 32
    return json.dumps({"fahrenheit": round(fahrenheit, 2)})


# In[30]:


# Function definition for the LLM
functions = [
    {
        "name": "convert_c_to_f",
        "description": "Convert Celsius to Fahrenheit",
        "parameters": {
            "type": "object",
            "properties": {
                "celsius": {
                    "type": "string"
                }
            },
            "required": ["celsius"]
        }
    }
]


# In[31]:


# User message
messages = [
    {
        "role": "user",
        "content": "Convert 40 Celsius to Fahrenheit"
    }
]


# In[32]:


# Ask the LLM
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions,
    function_call="auto"
)


# In[33]:


# Get function arguments
args = json.loads(response["choices"][0]["message"]["function_call"]["arguments"])


# In[34]:


# Run the function
result = convert_c_to_f(args["celsius"])


# In[35]:


# Add function call and result to the conversation
messages.append(response["choices"][0]["message"])
messages.append({
    "role": "function",
    "name": "convert_c_to_f",
    "content": result
})


# In[36]:


# Get the final response
final_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

print(final_response["choices"][0]["message"]["content"])


# In[ ]:




