import random
import time

def user_turn():
    print("Its your turn, you have 1 round in a 6 round chamber")
    user_choice = input("Press the trigger or aim at the bot? (trigger/bot): ").lower() #Makes the user choose between shooting at the bot or himself
    if user_choice == "trigger":
        print("You have decided to pull the trigger..")
        time.sleep(1)
        death = random.choice([True, False, False, False, False, False]) #Death chance is always 1:6
        if death == True:
            print("You have died, Bot wins!")
            play_choice = input("Wish to play again? (y/n)").lower()
            if play_choice == "y":
                print(play_again())
            else:
                print("See you next time!")
            def play_again(): #Asks the user if he wishes to play again
                play_again_choice = input("Do you wish to play again? (y/n): ").lower()
                if play_again_choice == "y":
                    print(user_turn())
                else:
                    print("Thanks for playing!")
                play_again()
        else:
            print("You have survived, its now the Bot`s turn..") 
            def bot_turn(): #Starts the bot turn
             print("The bot is deciding..")    
             time.sleep(2)
             bot_choice = random.choice(["trigger", "himself"]) #Makes the bot choose between shooting the player or himself
             if bot_choice == "trigger":
                print("The bot has decided to pull the trigger..")
                time.sleep(1)
                bot_user_kill = random.choice([True, False, False, False, False, False]) #Bot death chance 1:6
                if bot_user_kill == True:
                     print("The bot has killed you!")
                     print(play_again())
                else:
                  keep_playing2 =  input("The gun didnt go off, keep playing? (y/n): ").lower() #Asks the user if he wishes to continue playing if bot didnt kill him
                  if keep_playing2 == "y":
                      print(play_again())
                  else:
                      print("See you next time!")
             else:
                 print("The bot has chosen to aim at himself..")
                 time.sleep(1)
                 bot_self_death = random.choice([True, False, False, False, False, False]) 
                 if bot_self_death == True:
                     print("The bot died, you win!")
                     print(play_again())
                 else:
                    bot_survive_choice = input("The bot has survived, play again? (y/n)").lower()
                    if bot_survive_choice == "y":
                        print(user_turn())
                    else:
                        print("See you next time!")

            bot_turn()  
    elif user_choice == "bot": #Called if the user decided to shoot at the bot
        print("You have decided to aim at the bot..")
        time.sleep(1)
        bot_aim_death =  random.choice([True, False, False, False, False, False]) 
        if bot_aim_death == True:
            print("You have killed the bot, you win!")
            want_play_again = input("Do you want to keep playing? (y/n): ").lower()
            if want_play_again == "y":
                print(play_again())
            else:
                print("See you next time!")

        else:  
            print("The bot has survived!")
            want_play_again1 = input("Do you wish to keep playing? (y/n)").lower()
            if want_play_again1 == "y":
                print(play_again())
            else:
                print("See you next time!")
    else: #Used if user inputs anything other than trigger or bot
        print("Please choose between trigger or bot")
        print(user_turn()) #Takes user back to start
user_turn()



