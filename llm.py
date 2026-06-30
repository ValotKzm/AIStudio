from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def ask(system_prompt: str, user_prompt: str):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"\n LLM error: {e}")
        return "The AI could not generate a response."
