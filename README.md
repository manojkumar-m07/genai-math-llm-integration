## Integration of a Mathematical Calulations with a Chat Completion System using LLM Function-Calling

### AIM:
To design and implement a Python function for converting temperature from **Celsius to Fahrenheit**, and integrate it with a chat completion system using the **function-calling feature** of a Large Language Model (LLM).
### PROBLEM STATEMENT:
You need to create a Python program that can intelligently convert Celsius to Fahrenheit by leveraging OpenAI's function calling capability.
### DESIGN STEPS:
1. **Define the Function:** Create a Python function `celsius_to_fahrenheit()` to convert a Celsius temperature into Fahrenheit.

2. **Create the Function Schema:** Define the function's name, description, and input parameter (`celsius`) using JSON schema so the LLM can identify and call it.

3. **Process the User Request:** Send the user's query to the LLM. The model recognizes that a temperature conversion is needed and generates a function call with the required argument.

4. **Execute and Display the Result:** Extract the function arguments, execute the Python function, and display the converted temperature in Fahrenheit as the output.

### PROGRAM:
### DEVELOPED BY : Manojkumar M
### REGISTER NO. : 212225040226
```
import os
import json
import openai
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to convert Celsius to Fahrenheit
def convert_c_to_f(celsius):
    fahrenheit = (float(celsius) * 9/5) + 32
    return json.dumps({"fahrenheit": round(fahrenheit, 2)})

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

# User message
messages = [
    {
        "role": "user",
        "content": "Convert 37 Celsius to Fahrenheit"
    }
]

# Ask the LLM
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions,
    function_call="auto"
)

# Get function arguments
args = json.loads(response["choices"][0]["message"]["function_call"]["arguments"])

# Run the function
result = convert_c_to_f(args["celsius"])

# Add function call and result to the conversation
messages.append(response["choices"][0]["message"])
messages.append({
    "role": "function",
    "name": "convert_c_to_f",
    "content": result
})

# Get the final response
final_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

print(final_response["choices"][0]["message"]["content"])
```
### OUTPUT:

<img width="622" height="87" alt="image" src="https://github.com/user-attachments/assets/ed36a493-a2a4-415e-904a-ec7b09f6616d" />

### RESULT:
Hence, the Python program to design and implement a Python function for converting Celsius to Fahrenheit, integrating it with a chat completion system utilizing the function-calling feature of a large language model (LLM), is written successfully and executed.
