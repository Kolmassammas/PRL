import random
import PySimpleGUI as sg
from time import sleep

def getEnglishWord(choicenumber):
    jarj2 = []
    with open("englishwords.txt", "r", encoding="UTF8") as f2:
        for line in f2:
            line = line.strip()
            jarj2.append(line)

    return jarj2[choicenumber]


def getRussianWord(choicenumber):
    jarj = []
    with open("russianwords.txt", "r", encoding="UTF8") as f:
        for line in f:
            line = line.strip()
            jarj.append(line)
        
    return jarj[choicenumber]


def main():
    while True:
        choicenumber = random.randint(0, 9197)
        print(getRussianWord(choicenumber))
        print(getEnglishWord(choicenumber))
        sleep(1)



if __name__ == "__main__":
    main()
