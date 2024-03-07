from gpt4all import GPT4All
from typing import Tuple

class AI_Chat:
    def __init__(self):
        self._model = GPT4All("Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf", device="cpu")
        self._system_template = 'You are a medical assistant. Please analyse the data below and give a brief recommendation.'
        self._prompt_template = 'USER: {0}\nASSISTANT: '

    def generate_recommandation(self, age:int, gender: str, height: float, weight: float, hr: int, rr:str, ss: str, bp:Tuple[int, int]):
        prompt = self._system_template + self._prompt_template.format(f"Age: {age},Gender: {gender},Height: {height}cm,Weight: {weight}kg,Heart Rate: {hr}/min,Respiratory Rate: {rr}/min,Smoking Status: {ss},Blood Pressure: {bp[0]}/{bp[1]} mm[Hg]")
        return self._model.generate(prompt, max_tokens=100)