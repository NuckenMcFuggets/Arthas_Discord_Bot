import random

quotes = ["Frostmourne yearns.", "You will all serve me.", "I am one cold, brother.", ]
quotes_len = len(quotes)


def handle_response(message) -> str:
    p_message = message.lower()

    if(p_message == '!hello'):
        return 'THIS WHOLE DISCORD MUST BE PURGED.'
    

    if(p_message == 'roll'):
        return str(random.randint(0, 100))
    

    if(p_message == '!help'):
        return "`this is a help message`"

    if(p_message == '!quote'):
        
        i = random.randint(0, quotes_len)

        if(i <= quotes_len):
            return str(quotes[i])
    



        