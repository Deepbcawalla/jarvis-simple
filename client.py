#import google.generativeai as genai 

#genai.configure(api_key="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 ")  # Replace with your actual API key

#model = genai.GenerativeModel("gemini-2.5-flash")       
#response = model.generate_content("You are a virtual assistant named Jarvis.")      
#print(response.text)  
from openai import OpenAI
client = OpenAI(
    api_key="",

)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role":"system", 
            "content": "you are a virtual assistent name jarvis skilled in genaral task like alexa and google cloud"
        },
        {
            "role": "user",
            "content": "What is coding."
        }
    ]
)

print(completion.choices[0].message.content)