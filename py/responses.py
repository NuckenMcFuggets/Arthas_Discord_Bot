import random

quotes = ["Frostmourne yearns.", "You will all serve me.", "I am one cold, brother.", "I'm afraid my condition has left me cold to your pleas of mercy.", "No man can defeat me! Although, ten to twenty-five might do the trick."
          ,"If you think I'm powerful now, you should see my abilities in Heroic mode.","It's Lich King... not Lick King. The two are very very different jobs.", "I'm looking for a few dead men, with the cursed metal to be death knights."
          ,"All I want is to settle down with a Lich Queen of my own and have some little Lich-lings. Is that too much to ask?", "Ever get the feeling you're hearing voices in your helmet?", "You would make an adequate ghoul. Mindless and proficient at repetitive tasks."
          ,"The thing no one tells you about sitting on a frozen throne is how much of your flesh ends up stuck to it.", "I rule.", "Darkness stopped calling. It's alright though, we're still friends through Real ID."]

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
    



        