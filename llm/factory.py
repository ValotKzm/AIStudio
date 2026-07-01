from config import settings

from llm.providers.ollama_provider import OllamaProvider
from llm.providers.openai_provider import OpenAIProvider


PROVIDERS = {
    "openai": OpenAIProvider(),
    "ollama": OllamaProvider(),
}

def ask(system_prompt: str, user_prompt: str) -> str:

    provider = PROVIDERS.get(settings.default_provider)

    if provider is None:
        raise ValueError(f"Unknown LLM provider: {settings.default_provider}")
    
    return provider.ask(system_prompt, user_prompt)
