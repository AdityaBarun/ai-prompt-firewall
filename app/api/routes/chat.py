from fastapi import APIRouter

from app.application.services.chat_service import ChatService
from app.application.services.prompt_validator import PromptValidator
from app.domain.models.chat_models import ChatRequest, ChatResponse
from app.domain.rules.prompt_injection_rule import PromptInjectionRule
from app.infrastructure.llm.huggingface_provider import HuggingFaceProvider

router = APIRouter(prefix="/chat", tags=["Chat"])

provider = HuggingFaceProvider()
validator = PromptValidator(
    rules=[
        PromptInjectionRule(),
    ]
)

chat_service = ChatService(
    provider=provider,
    validator=validator,
)


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    response = await chat_service.process_prompt(request.prompt)

    return ChatResponse(response=response)