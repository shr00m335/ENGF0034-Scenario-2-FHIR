# ENGF0034-Scenario-2-FHIR
ENGF0034 Scenario 2 Group 1

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
4. Run the server
```
python server.py [port] [openai|gpt4all]
```
- Can choose between Open AI Chat GPT 3.5 or GPT4All
    - Open AI: Open AI Api key is required
    - GPT4All: Running LLM locally. Require CPUs which support AVX/AVX2 and at least 8GB of RAM

### 2. Test login data

|username|password|
|-|-|
|Oliver Lucas Ducey|password|
|Leigh Orla Mclean|123456|
