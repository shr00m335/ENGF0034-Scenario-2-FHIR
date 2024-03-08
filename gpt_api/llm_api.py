from abc import abstractmethod

class LLM_Api:
    def __init__(self):
        self._custom_instruction: str = None

    def set_custom_instruction(self, instruction: str):
        self._custom_instruction = instruction

    @abstractmethod
    def generate_response(self, prompt: str):
        pass