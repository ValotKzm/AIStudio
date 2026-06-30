from config import LLM_PROVIDER

from llm.providers.ollama_provider import ask as ollama_ask
from llm.providers.openai_provider import ask as openai_ask

def ask(system_prompt: str, user_prompt: str) -> str:

    if LLM_PROVIDER == "openai":
        return openai_ask(system_prompt, user_prompt)
    
    if LLM_PROVIDER == "ollama":
        return ollama_ask(system_prompt, user_prompt)
    
    raise ValueError(f"Unknown LLM provider: {LLM_PROVIDER}")