from typing import Dict, List

class Patient:
    def __init__(self, data: Dict):
        self._id: str = data["id"]
        self._family_name: str = data["name"][0]["family"]
        self._given_name: List[str] = data["name"][0]["given"]
        self._gender: str = data["gender"]
        self._birth_date = data["birthDate"]
        self._telecom = data["telecom"]

    def __repr__(self) -> str:
        return f"<Patient name='{self._given_name[0]} {self._family_name}'>"
    
    @property
    def id(self) -> str:
        return self._id