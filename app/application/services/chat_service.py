from app.application.interfaces.llm_provider import BaseLLMProvider
from app.application.services.prompt_validator import PromptValidator


class ChatService:
    def __init__(
        self,
        provider: BaseLLMProvider,
        validator: PromptValidator,
    ):
        self.provider = provider
        self.validator = validator

    async def process_prompt(self, prompt: str) -> str:
        is_valid, reason = self.validator.validate(prompt)

        if not is_valid:
            return f"BLOCKED: {reason}"

        return await self.provider.generate(prompt)