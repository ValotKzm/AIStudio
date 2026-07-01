from openai import OpenAI
from config import settings

from llm.base import BaseProvider


class OpenAIProvider(BaseProvider):    

    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)

    def ask(
        self,
        model: str,
        system_prompt: str, 
        user_prompt: str,
    ) -> str:
        
        try:
            response = self.client.chat.completions.create(
                model=model,
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
