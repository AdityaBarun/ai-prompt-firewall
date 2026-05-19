from app.providers.factory import ProviderFactory


class GatewayService:

    @staticmethod
    async def process_request(
        provider_name: str,
        prompt: str
    ):

        provider = ProviderFactory.get_provider(
            provider_name
        )

        response = await provider.generate(prompt)

        return response