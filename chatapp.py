import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def structured_generator(prompt):
    model = genai.GenerativeModel("gemini-2.5-pro") 
    response = model.generate_content(prompt)
    return response.text
