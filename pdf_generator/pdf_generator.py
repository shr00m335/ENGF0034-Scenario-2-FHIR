from xhtml2pdf import pisa

import jinja2
from datetime import datetime

def html_template(name, age, phone, address):
    my_name = name
    my_age = age
    my_phone_number = phone
    my_address = address
    medication1 = "med1"
    medication2 = "med2"
    medication3 = "med3"
    health1 = "h1"
    health2 = "h2"
    health3 = "h3"
    health4 = 'h4'
    today_date = datetime.today().strftime("%d %b, %Y")

    context = {"my_name": my_name, "my_age" :my_age, "my_phone_number": my_phone_number, "my_address": my_address,
               "medication1" : medication1, 'medication2': medication2, "medication3": medication3,
                "health1": health1, "health2":health2, "health3": health3, "health4": health4,
                "today_date": today_date}

    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader= template_loader)

    template = template_env.get_template("data.html")
    output_text = template.render(context)

    with open(my_name + "_information.pdf", "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(output_text, dest=pdf_file)
        
    return not pisa_status.err



Name = "jack"
age = 19
phone = 123456
address = "london, united kingdom"


html_template(Name, age, phone, address)
