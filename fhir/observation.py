from .loinc_code import LoincCode

class Observation:
    def __init__(self, data):
        self._code = data["code"]["coding"][0]["code"]
        self._text = data["code"]["text"]
        self._issued_time = data["issued"]
        if "component" in data:
            self._value = [x["valueQuantity"]["value"] for x in data["component"]]
            self._unit = data["component"][0]["valueQuantity"]["unit"]
        elif "valueQuantity" in data:
            self._value = [data["valueQuantity"]["value"]]
            self._unit = data["valueQuantity"]["unit"]
        else:
            print(data)
            self._value = data["valueCodeableConcept"]["text"]
            self._unit = None
        

    def __repr__(self) -> str:
        return f"<Observation code={self._code} name=\"{self._text}\" value={self._value}>"
    
    def to_string(self) -> str:
        if self._code in [LoincCode.BLOOD_PRESSURE]:
            return f"{self._value[1]}/{self._value[0]} {self._unit}"
        elif self._code in [LoincCode.BODY_MASS_INDEX_PER_PERCENTILE, LoincCode.HEART_RATE, LoincCode.RESPIRATORY_RATE]:
            return f"{self._value[0]}{self._unit}"
        elif self._code in [LoincCode.SMOKING_STATUS]:
            return self._value
        else:
            return f"{self._value[0]} {self._unit}"
    
    def to_json(self):
        return {
            "item": self._text,
            "value": self._value,
            "unit": self._unit,
            "time": self._issued_time
        }
    
    @property
    def code(self) -> str:
        return self._code
    
    @property
    def issued_date(self) -> str:   
        return self._issued_time