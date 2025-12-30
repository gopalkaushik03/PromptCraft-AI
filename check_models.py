import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# We use the variable name exactly as it is in your .env file
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Error: GOOGLE_API_KEY not found in .env file.")
else:
    genai.configure(api_key=api_key)
    print("Checking available models for your API key...")
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"✅ Available: {m.name}")
    except Exception as e:
        print(f"❌ Error checking models: {e}")
        