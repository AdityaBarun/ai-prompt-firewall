from abc import ABC, abstractmethod


class PromptRule(ABC):
    @abstractmethod
    def detect(self, prompt: str) -> bool:
        pass

    @property
    @abstractmethod
    def reason(self) -> str:
        pass