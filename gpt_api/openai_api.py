from openai import OpenAI
from .llm_api import LLM_Api
import os
from dotenv import load_dotenv


class OpenAIAPI(LLM_Api):
    def __init__(self) -> None:
        super().__init__()
        load_dotenv()
        api_key = os.getenv('OPENAI_KEY')
        self._client: OpenAI = OpenAI(api_key=api_key)

    def get_response(self, prompt: str) -> str:
        if self._custom_instruction:
            prompt = f'{self._custom_instruction}\n\n{prompt}'

        response = self._client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt}]
        )

        return response.choices[0].message.content.strip()