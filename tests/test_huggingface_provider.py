import pytest

from app.infrastructure.llm.huggingface_provider import HuggingFaceProvider


@pytest.mark.asyncio
async def test_huggingface_provider_generate():
    provider = HuggingFaceProvider()

    response = await provider.generate(
        "Explain Python decorators"
    )

    assert isinstance(response, str)