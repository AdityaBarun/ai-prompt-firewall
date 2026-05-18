from app.domain.models.chat_models import ChatRequest, ChatResponse


def test_chat_request_model():
    request = ChatRequest(
        prompt="Explain Redis"
    )

    assert request.prompt == "Explain Redis"


def test_chat_response_model():
    response = ChatResponse(
        response="Hello"
    )

    assert response.response == "Hello"