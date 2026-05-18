import os

import httpx
from dotenv import load_dotenv

from app.application.interfaces.llm_provider import BaseLLMProvider

load_dotenv()


class HuggingFaceProvider(BaseLLMProvider):
    def __init__(self):
        self.api_key = os.getenv("HUGGINGFACE_API_KEY")

        self.model = os.getenv(
            "HF_MODEL",
            "mistralai/Mistral-7B-Instruct-v0.2"
        )

        self.base_url = (
            f"https://api-inference.huggingface.co/models/{self.model}"
        )

    async def generate(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 200,
                "temperature": 0.7
            }
        }

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                self.base_url,
                headers=headers,
                json=payload
            )

            response.raise_for_status()

        data = response.json()

        if isinstance(data, list):
            return data[0].get("generated_text", "")

        return "No response generated"