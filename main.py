import random


def main():

    jarj = []
    with open("russianwords.txt", "r", encoding="UTF8") as f:
        for line in f:
            line = line.strip()
            jarj.append(line)

    jarj2 = []
    with open("englishwords.txt", "r", encoding="UTF8") as f2:
        for line in f2:
            line = line.strip()
            jarj2.append(line)
            
            
    choicenumber = random.randint(0, len(jarj))
    
    print(jarj[choicenumber])
    print(jarj2[choicenumber])

    
    
    
    
    
if __name__ == "__main__":
    main()