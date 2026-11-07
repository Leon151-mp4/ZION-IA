#imports of modules
from commands.comands import commandsList, data
from brain.model import dataList, state, checkState, NeuralNetwork
#imports of librarys
import random
import os


#logo
os.system("clear")
logo = [r"  ________  ______   ______  __    __         ______   ______ ",  
        r" |        \|      \ /      \|  \  |  \       |      \ /      \ ", 
        r" \$$$$$$$$ \$$$$$$|  $$$$$$\| $$\ | $$       \$$$$$$ | $$$$$$\ ",
        r"    /  $$   | $$  | $$  | $$| $$$\| $$        | $$   |$$__| $$ ",
        r"   /  $$    | $$  | $$  | $$| $$$$\ $$        | $$   |$$    $$ ",
        r"  /  $$     | $$  | $$  | $$| $$\$$ $$        | $$   |$$$$$$$$ ",
        r" /  $$___  _| $$_ | $$__/ $$| $$ \$$$$       _| $$_  |$$  | $$ ",
        r"|  $$    \|   $$ \ \$$    $$| $$  \$$$      |   $$ \ |$$  | $$ ",
        r" \$$$$$$$$ \$$$$$$  \$$$$$$  \$$   \$$       \$$$$$$ \$$   \$$ "]
                                                              
for i in logo:
    print(i)                                                              
                                                           
print("Welcome to ZION IA a IA Open-Source project ")
print("Type >> help << for more information")

print("")
print("")


#CONTROL CENTER: WHERE MAIN CONTROLS THE SHOW.
#That part of the code decide if the system
#is idle or working and due a lot of things
def checkData(dataList):
    if not dataList:
        return (True, "idle")
    elif dataList:
        return (True, "Working")
state["system"] = checkData(dataList)
#first while true
returnValue = None
while True:
    inputValue = input(">> :")


    dataChannel = dataList.append(inputValue)
    state["system"] = checkData(dataList)
    checkState(state)

    data["input"] = inputValue
    #ifs and elses
    if inputValue in commandsList:
        returnValue = commandsList[inputValue](data)
        
        data["return"] = returnValue

    if returnValue == (True, "exit"):
        break

    if returnValue == (True, "showslogo"):
        for i in logo:
            print(i)
