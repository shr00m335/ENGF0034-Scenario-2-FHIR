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