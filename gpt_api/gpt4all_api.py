from gpt4all import GPT4All
from typing import Tuple
from .llm_api import LLM_Api

class GPT4All_Api(LLM_Api):
    def __init__(self):
        super().__init__()
        self._model = GPT4All("mistral-7b-openorca.gguf2.Q4_0.gguf", device="cpu")
        self._prompt_template = 'USER: {0}\nASSISTANT: '

    def get_response(self, prompt: str):
        prompt = self._custom_instruction + self._prompt_template.format(prompt)
        return self._model.generate(prompt, max_tokens=300)