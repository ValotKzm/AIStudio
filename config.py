from dotenv import load_dotenv
import os

load_dotenv()

# LLM configuration
LLM_PROVIDER = os.getenv("LLM_PROVIDER")
MODEL = os.getenv("MODEL")

# OpenAI configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Configuration validation
if LLM_PROVIDER is None:
    raise ValueError("LLM_PROVIDER is missing from the .env file.")

if MODEL is None:
    raise ValueError("MODEL is missing from the .env file.")

