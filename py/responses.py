import random


def handle_response(message) -> str:
    p_message = message.upper()

    if(p_message == 'hello'):
        return 'THIS WHOLE DISCORD MUST BE PURGED.'
    

    if(p_message == 'roll'):
        return str(random.randint(0, 100))
    

    if(p_message == '!help'):
        return "`this is a help message`"