from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

from llm.base import BaseProvider


class OpenAIProvider:    

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def ask(self, system_prompt: str, user_prompt: str):
        try:
            response = self.client.chat.completions.create(
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
