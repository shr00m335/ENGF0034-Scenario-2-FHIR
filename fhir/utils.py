from functools import wraps
import time

def fhir_api_endpoint(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if time.time() > self._expires:
            self._authorize()
        return func(self, *args, **kwargs)
    return wrapper