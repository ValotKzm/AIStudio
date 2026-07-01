from ollama import chat

from llm.base import BaseProvider


class OllamaProvider(BaseProvider):

    def ask(
        self,
        model: str,
        system_prompt: str,
        user_prompt: str,
        ) -> str:

        try:
            response = chat(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
                    },
                ],
            )

            return response.message.content
        
        except Exception as e:
            print(f"\n LLM error: {e}")
            return "The AI could not generate a response."
    