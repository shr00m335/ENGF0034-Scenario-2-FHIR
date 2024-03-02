from typing import Dict, List

class Patient:
    def __init__(self, data: Dict):
        self._family_name: str = data["name"][0]["family"]
        self._given_name: List[str] = data["name"][0]["given"]

    def __repr__(self) -> str:
        return f"<Patient name='{self._given_name[0]} {self._family_name}'>"