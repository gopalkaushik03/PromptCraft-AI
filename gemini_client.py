import google.generativeai as genai
import os
import sys
from dotenv import load_dotenv

# ==========================================
# 1. API & MODEL SETUP
# ==========================================
load_dotenv() 

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("❌ CRITICAL ERROR: GOOGLE_API_KEY not found. Check your .env file.")
else:
    genai.configure(api_key=api_key)

# --- AUTO-DETECT MODEL FUNCTION ---
def get_working_model_name():
    try:
        if not api_key: return "models/gemini-1.5-flash"
        my_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        # Priority: Pro (Better Logic) -> Flash (Faster)
        priority_list = [
            "models/gemini-1.5-pro",
            "models/gemini-pro",
            "models/gemini-1.5-flash"
        ]
        
        for priority in priority_list:
            if priority in my_models: return priority
        return my_models[0] if my_models else "models/gemini-1.5-flash"
        
    except Exception as e:
        print(f"⚠️ Error listing models: {e}")
        return "models/gemini-1.5-flash"

CURRENT_MODEL_NAME = get_working_model_name()
print(f"✅ Using Model: {CURRENT_MODEL_NAME}")

# ==========================================
# 2. REFINER AGENT (NOW AUTO-DETECTS DEPTH)
# ==========================================
def refine_prompt(user_raw_input):
    """
    Refines the prompt. Auto-detects if user needs short vs long answer.
    """
    model = genai.GenerativeModel(CURRENT_MODEL_NAME)
    
    meta_prompt = f"""
    You are an expert Prompt Engineer. 
    Analyze the user's request and rewrite it into a professional, optimized prompt.
    
    User Request: "{user_raw_input}"
    
    1. **Detect Intent:** - If the user asks "what is", "define", or "briefly", rewrite the prompt to ask for a concise, 1-paragraph definition.
       - If the user asks for "code", "guide", "explain", "essay", or a complex topic, rewrite the prompt to demand a comprehensive, detailed, step-by-step response (minimum 1000 words).
    
    2. **Optimization:**
       - Add context, persona (e.g., "Act as an Expert"), and output format (e.g., "Use bullet points", "Show code examples").
    
    Rules: 
    - Do not answer the question. 
    - ONLY output the rewritten prompt.
    """
    
    try:
        response = model.generate_content(meta_prompt)
        return response.text
    except Exception as e:
        return f"Error refining prompt: {e}"

# ==========================================
# 3. EXECUTOR AGENT
# ==========================================
def generate_response_stream(prompt, system_instruction, temperature, max_tokens, top_p):
    try:
        generation_config = genai.types.GenerationConfig(
            temperature=temperature,
            max_output_tokens=max_tokens,
            top_p=top_p
        )

        model = genai.GenerativeModel(
            CURRENT_MODEL_NAME,
            system_instruction=system_instruction
        )

        response = model.generate_content(prompt, stream=True, generation_config=generation_config)

        for chunk in response:
            if chunk.text:
                yield chunk.text

    except Exception as e:
        if "429" in str(e):
            yield "⚠️ **Rate Limit Hit**: Please wait 15-30 seconds."
        else:
            yield f"❌ Error: {str(e)}"