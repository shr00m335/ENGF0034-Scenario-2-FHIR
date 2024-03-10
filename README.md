# Medical Insight Platform
ENGF0034 Scenario 2 Group 1

Our project involves the development of a healthcare website utilizing the Fast Healthcare Interoperability Resources (FHIR) API. Our website serves as a platform for both patients and medical officers to access and analyze patients' health data, which is a summarized version of patients' past medical records. The unique feature of this website is the use of generative AI to provide personalized health recommendations based on the data obtained from the FHIR API. This not only provides patients with insights into their health but also assists medical officers in diagnosis. Our project aims to improve patient care and the efficiency of the medical system by integrating technology with healthcare, promoting proactive health management and encouraging a collaborative environment between patients and healthcare providers.

### 1. How to run
1. Clone this repository
```
git clone https://github.com/shr00m335/ENGF0034-Scenario-2-FHIR.git
```
2. Create a .env file and put your FHIR API client id and client secret in it
```
CLIENT_ID={your client id}
CLIENT_SECRET={your client secret}
OPENAI_KEY="{add key here}"
```
3. Install required Python libraries 
```
pip install -r requirements.txt
```
- It is recommanded to create a new environment
4. Run the server
```
python server.py [port] [openai|gpt4all]
```
- Can choose between Open AI Chat GPT 3.5 or GPT4All
    - Open AI: Open AI Api key is required
    - GPT4All: Running LLM locally with the mistral-7b-openorca model. 
        - Requires at least 4GB of storage either of the following
            - CPUs which support AVX/AVX2 and at least 8GB of RAM
            - GPUs with at least 4GB of VRAM

### 2. Test login data

|username|password|
|-|-|
|Oliver Lucas Ducey|password|
|Leigh Orla Mclean|123456|
