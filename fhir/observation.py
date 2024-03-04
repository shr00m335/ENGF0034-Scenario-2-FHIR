class Observation:
    def __init__(self, data):
        self._code = data["code"]["coding"][0]["code"]
        self._text = data["code"]["text"]
        self._issued_time = data["issued"]
        self._value = data["valueQuantity"]["value"]
        self._unit = data["valueQuantity"]["unit"]

    def __repr__(self) -> str:
        return f"<Observation code={self._code} name=\"{self._text}\" value={self._value}>"