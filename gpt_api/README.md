# engf34-scenario-2

## Setup

Install the requirements

```
pip install -r requirements.txt
```

Create a `.env` file, and then add the following line

```
OPENAI_KEY="{add key here}"
```

## Example usage

```python
from openai_api import OpenAIAPI

gpt_api = OpenAIAPI()

instruction = 'Start your sentence with "Hello there!"'
gpt_api.set_custom_instruction(instruction)

prompt = 'How are you?'
response = gpt_api.get_response(prompt)
print(f'gpt-3.5-turbo: {response}')
```