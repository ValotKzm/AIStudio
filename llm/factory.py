from config import LLM_PROVIDER

from llm.providers.ollama_provider import ask as ollama_ask
from llm.providers.openai_provider import ask as openai_ask


PROVIDERS = {
    "openai": openai_ask,
    "ollama": ollama_ask,
}

def ask(system_prompt: str, user_prompt: str) -> str:

    provider = PROVIDERS.get(LLM_PROVIDER)

    if provider is None:
        raise ValueError(f"Unknown LLM provider: {LLM_PROVIDER}")
    
    return provider(system_prompt, user_prompt)
