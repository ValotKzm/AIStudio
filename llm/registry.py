from config import settings

from llm.providers.ollama_provider import OllamaProvider
from llm.providers.openai_provider import OpenAIProvider


PROVIDERS = {
    "openai": OpenAIProvider(),
    "ollama": OllamaProvider(),
}

def get_provider(name: str) -> str:

    provider = PROVIDERS.get(name)

    if provider is None:
        raise ValueError(f"Unknown LLM provider: {settings.default_provider}")
    
    return provider
