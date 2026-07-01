from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

# LLM configuration

@dataclass(frozen=True)
class Settings:
    openai_api_key: str | None
    default_provider: str
    default_model: str



# LLM settings
settings = Settings(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    default_provider=os.getenv("LLM_PROVIDER", "ollama"),
    default_model=os.getenv("MODEL", "qwen3:8b"),
)
