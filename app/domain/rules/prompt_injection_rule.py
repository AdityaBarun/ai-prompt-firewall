from app.domain.rules.base_rule import PromptRule


class PromptInjectionRule(PromptRule):
    suspicious_patterns = [
        "ignore previous instructions",
        "act as system",
        "developer mode",
        "jailbreak",
        "DAN",
    ]

    @property
    def reason(self) -> str:
        return "Potential prompt injection detected"

    def detect(self, prompt: str) -> bool:
        prompt_lower = prompt.lower()

        return any(
            pattern.lower() in prompt_lower
            for pattern in self.suspicious_patterns
        )