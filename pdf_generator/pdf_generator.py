from xhtml2pdf import pisa

import jinja2
from datetime import datetime

def html_template(ID,
    FAMILY_NAME, 
    GIVEN_NAME, 
    GENDER, 
    BIRTH_DATE, 
    TELECOM, 
    ADDRESS, 
    MEDICAL_RECORD_NUMBER, 
    BODY_MASS_INDEX, 
    HEIGHT,
    WEIGHT, 
    HEART_RATE, 
    RESPIRATORY_RATE, 
    SMOKING_STATUS,
    BODY_TEMPERATURE,
    BODY_MASS_INDEX_PER_PERCENTILE,
    BLOOD_PRESSURE):
    
    today_date = datetime.today().strftime("%d %b, %Y")

    context = {"my_ID" : ID,
        "family_name": FAMILY_NAME, 
        "given_name" : GIVEN_NAME, 
        "gender": GENDER, 
        "birth_date": BIRTH_DATE, 
        "telecom": TELECOM, 
        "address" : ADDRESS, 
        "medical_record_number": MEDICAL_RECORD_NUMBER, 
        "body_mass_index": BODY_MASS_INDEX, 
        "height" : HEIGHT, 
        "weight" : WEIGHT, 
        "heart_rate":HEART_RATE, 
        "respiratory_rate":RESPIRATORY_RATE, 
        "smoking_status":SMOKING_STATUS,
        "body_temperature":BODY_TEMPERATURE,
        "body_mass_index_per_percentile": BODY_MASS_INDEX_PER_PERCENTILE,
        "blood_pressure": BLOOD_PRESSURE,
        "today_date": today_date}

    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader= template_loader)

    template = template_env.get_template("/data.html")
    output_text = template.render(context)

    with open( GIVEN_NAME + "_information.pdf", "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(output_text, dest=pdf_file)
        
    return not pisa_status.err

#patient background
ID = 123
FAMILY_NAME = "Mok"
GIVEN_NAME = "Jack"
GENDER = "M"
BIRTH_DATE = 2004
TELECOM = "gmail.com"
ADDRESS = "london"
MEDICAL_RECORD_NUMBER = 1234

#medical conditions
BODY_MASS_INDEX = 20
HEIGHT = 150
WEIGHT = 50
HEART_RATE = 100
RESPIRATORY_RATE = 50
SMOKING_STATUS = "yes"
BODY_TEMPERATURE = 20
BODY_MASS_INDEX_PER_PERCENTILE = 22
BLOOD_PRESSURE = 90

html_template(
    ID,
    FAMILY_NAME, 
    GIVEN_NAME, 
    GENDER, 
    BIRTH_DATE, 
    TELECOM, 
    ADDRESS, 
    MEDICAL_RECORD_NUMBER, 
    BODY_MASS_INDEX, 
    HEIGHT, 
    WEIGHT, 
    HEART_RATE, 
    RESPIRATORY_RATE, 
    SMOKING_STATUS,
    BODY_TEMPERATURE,
    BODY_MASS_INDEX_PER_PERCENTILE,
    BLOOD_PRESSURE)
