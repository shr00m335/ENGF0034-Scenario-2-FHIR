import requests
from typing import Dict, Optional, List
from .patient import Patient
from .observation import Observation
from .utils import *
from .exceptions import UnauthorizedException
import os
from dotenv import load_dotenv
from .loinc_code import LoincCode

class FHIR_Api:
    _token: str
    _expires: str

    def __init__(self):
        load_dotenv()
        self._authorize()

    def _authorize(self) -> Dict[int, str]:
        url = "https://login.microsoftonline.com/1bea21f2-daf2-4600-bcf2-894467ed9fb0/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "resource": "https://gosh-synth-fhir.azurehealthcareapis.com/",
            "grant_type": "client_credentials",
            "client_id": os.getenv("CLIENT_ID"),
            "client_secret": os.getenv("CLIENT_SECRET")
        }

        res = requests.post(url, data, headers=headers)

        if res.status_code == 200:
            data = res.json()
            self._expires = int(data["expires_on"])
            self._token = data["access_token"]
        else:
            raise UnauthorizedException("Unable to obtain token")
    
    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self._token}"
        }
        
    @fhir_api_endpoint
    def get_patient_details(self, given_name: str, family_name: str) -> Optional[Patient]:
        url = "https://gosh-synth-fhir.azurehealthcareapis.com/Patient"
        params = {
            "family": family_name,
            "given": given_name
        }
        res = requests.get(url, params=params, headers=self._get_headers())
        if res.status_code != 200:
            return None
        data = res.json()
        if not "entry" in data.keys():
            return None
        return Patient(data["entry"][0]["resource"])
    
    @fhir_api_endpoint
    def get_patient_observation(self, patient: Patient, code: str):
        url = "https://gosh-synth-fhir.azurehealthcareapis.com/Observation"
        params = {
            "subject": f"Patient/{patient.id}",
            "code": f"http://loinc.org|{code}",
            "_sort": "-date",
            "_count": 9
        }
        res = requests.get(url, params=params, headers=self._get_headers())
        if res.status_code != 200:
            return []
        data = res.json()
        if not "entry" in data.keys():
            return []
        return [Observation(x["resource"]) for x in data["entry"]][0]
    
    @fhir_api_endpoint
    def get_patient_health_data(self, patient: Patient) -> List[Observation]:
        url = "https://gosh-synth-fhir.azurehealthcareapis.com/Observation"
        params = {
            "subject": f"Patient/{patient.id}",
            "code": f"http://loinc.org|{','.join(LoincCode.ALL_CODES)}",
            "_sort": "-date",
            "_count": 9
        }
        res = requests.get(url, params=params, headers=self._get_headers())
        if res.status_code != 200:
            return []
        data = res.json()
        if not "entry" in data.keys():
            return []
        return [Observation(x["resource"]) for x in data["entry"]]

if __name__ == "__main__":
    api = FHIR_Api()
    p = api.get_patient_details("Oliver Lucas", "Ducey")
    print(p)