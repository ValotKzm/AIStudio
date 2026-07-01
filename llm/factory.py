from config import LLM_PROVIDER

from llm.providers.ollama_provider import OllamaProvider
from llm.providers.openai_provider import OpenAIProvider


PROVIDERS = {
    "openai": OpenAIProvider(),
    "ollama": OllamaProvider(),
}

def ask(system_prompt: str, user_prompt: str) -> str:

    provider = PROVIDERS.get(LLM_PROVIDER)

    if provider is None:
        raise ValueError(f"Unknown LLM provider: {LLM_PROVIDER}")
    
    return provider.ask(system_prompt, user_prompt)
