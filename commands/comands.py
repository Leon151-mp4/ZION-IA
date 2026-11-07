
#imports
import os
import time
import datetime




#standard values
data = {
    "name": "Admin User"
}
#defs
def help(data):
    print("The ZION IA can do:")
    print("")
    print("To talk:\n"
        "Type what you wanna talk.\n")
    print("Search:\n"
          "NEWS -> by typing news. (not working for now)\n"
          "Top Trends and Videos and more -> Type screash someonething here. (not working for now)\n"
    )
    print("")
    print("User:\n"
          "setname -> set the name user\n"
          "whoiam -> shows what type of user you are and some informations.\n")
    print("")
    print("Utilities:\n"
          "clear -> clears the session but keeps the memory.\n"
          "time -> shows the current time.\n"
          "showslogo -> shows the logo."
          )
    print("System:")
    print("To exit -> type exit.")
    print("")
    print("Admin functions: \n"
        "learn -> the ZION IA start do due machine learning.\n"
        "forget -> forget a knowing of machine learning.\n"
        "memory -> shows what zion learning.\n"
        "debug -> debug mode ativation.\n"
        "To acess that funciton please have caution... ZION: ;-;.\n")
    return (True, 'help')




def hello(data):
    print("ZION: hellow! How i can assist your today?")
    return (True, 'hello')




def exit(data):
    print("")
    print("ZION: Bye Bye. Have a good day!")
    return (True, 'exit')




def debug(data):


    if data is not None:

        os.system("clear")
        time.sleep(0.5)

        print("_____ZION DEBUG MODE_____")
        print("comando digitado: ", data["input"])
        print("valor do retorno: ", data)
        print("Nome do usuario: ", data["name"])
    else:
        print("ZION: Loading, please type debug again...")

    return (True, 'debug')




def setname(data):

    print("Set your name user: ")
    question = input(">> :")

    print(f"Is {question} rigth? [y/n]")
    question1 = input(">> :")

    if question1 == "y":
        print("set name complete")
        data["name"] = question

    elif question1 == "n":
        print("Set your name user: ")
    else:
        print("Please try again.")
    return (True, 'setname')



def timer(data):
    print("ZION: Curret time: ", datetime.datetime.now())
    return (True, 'time')

def clear(data):
    os.system("clear")

    return (True, 'clear')



def whoiam(data):
    print("you are: ", data["name"])
    return (True, "whoiam")



def showslogo(data):
    return (True, "showslogo")

#comandlist
commandsList = {
    
        "hello": hello,
        "help": help,
        "exit": exit,
        "debug": debug,
        "setname": setname,
        "time": timer,
        "clear": clear,
        "whoiam": whoiam,
        "showslogo": showslogo
}
