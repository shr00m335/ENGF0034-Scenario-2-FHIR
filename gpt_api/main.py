from gpt_api import OpenAIAPI

def exit_program(gpt_api: OpenAIAPI) -> None:
    exit()

def set_custom(gpt_api: OpenAIAPI) -> None:
    print('Enter custom instruction (This is added before each prompt)')
    custom_instruction = input('> ')
    gpt_api.set_custom_instruction(custom_instruction)

def help(gpt_api: OpenAIAPI) -> None:
    for command in COMMANDS:
        print(f'- /{command}')

COMMANDS = {
    'exit': exit_program,
    'setcustom': set_custom,
    'help': help
}

def main() -> None:
    gpt_api = OpenAIAPI()
    while True:
        user_input = input('> ')

        # handle commands
        if user_input[:1] == '/':
            command = user_input[1:]
            if command not in COMMANDS:
                print('Invalid command! (Check commands using /help)')
            else:
                COMMANDS[command](gpt_api)
            continue

        response = gpt_api.get_response(user_input)
        print(f'gpt-3.5-turbo: {response}')

if __name__ == '__main__':
    main()