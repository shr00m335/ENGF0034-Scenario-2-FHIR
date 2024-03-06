from openai import OpenAI
import os
from dotenv import load_dotenv


class OpenAIAPI:
    def __init__(self, api_key: str=None) -> None:
        if api_key is None:
            load_dotenv()
            api_key = os.getenv('OPENAI_KEY')
        
        self._client: OpenAI = OpenAI(api_key=api_key)
        self._custom_instruction: str = None

    def set_custom_instruction(self, instruction: str) -> None:
        self._custom_instruction = instruction

    def get_response(self, prompt: str) -> str:
        if self._custom_instruction:
            prompt = f'{self._custom_instruction}\n\n{prompt}'

        response = self._client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt}]
        )

        return response.choices[0].message.content.strip()