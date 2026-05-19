import random
import time

from app.providers.base import BaseLLMProvider


class MockProvider(BaseLLMProvider):

    async def generate(self, prompt: str):

        start = time.time()

        simulated_latency = random.randint(50, 300)

        risk_score = round(
            random.uniform(0.05, 0.95),
            2
        )

        time.sleep(simulated_latency / 1000)

        return {
            "response": f"Processed prompt: {prompt}",
            "provider": "mock",
            "latency_ms": simulated_latency,
            "tokens_used": random.randint(20, 200),
            "risk_score": risk_score
        }