from typing import Dict, List

class Patient:
    def __init__(self, data: Dict):
        self._id: str = data["id"]
        self._family_name: str = data["name"][0]["family"]
        self._given_name: List[str] = data["name"][0]["given"]
        self._gender: str = data["gender"]
        self._birth_date = data["birthDate"]
        self._telecom = data["telecom"]
        # self._address = data[""]
        # self._mediacal_record_number = data[""]

    def __repr__(self) -> str:
        return f"<Patient name='{self._given_name[0]} {self._family_name}'>"
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def full_name(self) -> str:
        return f"{self._given_name[0]} {self._family_name}"
    
    @property
    def family_name(self) -> str:
        return self._family_name
    
    @property
    def given_name(self) -> str:
        return self._given_name[0]
    
    @property
    def gender(self) -> str:
        return self._gender
    
    @property
    def birth_date(self) -> str:
        return self._birth_date