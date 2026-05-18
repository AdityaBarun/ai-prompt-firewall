from typing import List

from app.domain.rules.base_rule import PromptRule


class PromptValidator:
    def __init__(self, rules: List[PromptRule]):
        self.rules = rules

    def validate(self, prompt: str) -> tuple[bool, str]:
        for rule in self.rules:
            if rule.detect(prompt):
                return False, rule.reason

        return True, "Valid prompt"