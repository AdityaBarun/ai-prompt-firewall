from app.providers.mock_provider import MockProvider


class ProviderFactory:

    @staticmethod
    def get_provider(provider_name: str):

        providers = {
            "mock": MockProvider()
        }

        provider = providers.get(provider_name)

        if not provider:
            raise ValueError(
                f"Unsupported provider: {provider_name}"
            )

        return provider