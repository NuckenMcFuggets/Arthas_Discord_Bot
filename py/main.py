import bot
if __name__ == '__main__':
    
    bot_choice = input("Enter which bot to run:")

    if(bot_choice == "1"):
        bot.run_bot()
    elif(bot_choice == "2"):
        bot.voice_bot()
    else:
        print("error")