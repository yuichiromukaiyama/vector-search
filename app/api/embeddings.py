from os import getenv
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv(".env")

OPENAI_KEY = getenv("OPENAI_KEY", "")
OPENAI_BASE_DOMAIN = getenv("OPENAI_BASE_DOMAIN", "")
OPENAI_API_VERSION = getenv("OPENAI_API_VERSION", "")
OPENAI_API_ENGINE = getenv("OPENAI_API_ENGINE", "")
OPENAI_EMBEDDINGS_API_ENGINE = getenv("OPENAI_EMBEDDINGS_API_ENGINE", "")

__client = AzureOpenAI(
    api_key=OPENAI_KEY,
    api_version=OPENAI_API_VERSION,
    azure_endpoint=OPENAI_BASE_DOMAIN,
)


def embeddings(input: str) -> list[float]:
    res = __client.embeddings.create(input=input, model=OPENAI_EMBEDDINGS_API_ENGINE)
    return res.data[0].embedding
