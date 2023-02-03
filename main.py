import random
from colorama import Fore, Back, Style

words = [ "viens", "divi", "tris", "cits"]
inGame = False
while True:
    totalLives = 5
    usedLives = 0
    word = random.choice(words)
    guessedWord = list("_" for _ in word) #(["_", "_", "_"])
    #print("".join(guessedWord))
    while (totalLives > 0 and not "".join(guessedWord) == word):
        inp = input("Ievade (burts): ")
        if (len(inp) < 1): continue
        if (len(inp) != len(word)): continue
        #inp = inp[0]

        guessedWord= list("_" for _ in word)
        for aaa in range(0, len(guessedWord)):
            if word[aaa] == inp[aaa]:
                guessedWord[aaa] = inp[aaa]
                print(f"{Fore.GREEN}{inp[aaa]}{Style.RESET_ALL}", end="")
            elif inp[aaa] in word:
                print(f"{Fore.YELLOW}{inp[aaa]}{Style.RESET_ALL}", end="")
            else:
                print(f"{inp[aaa]}", end="")
        print("")
        totalLives -= 1

        #print(didGuessLetter)
        #print("".join(guessedWord))
    if(totalLives > 0):
        print("Uzvara")
    else:
        print("Zaudējums")
    if input("Vai beigt spēli vai nē? (Y/N)")[0].lower() == "y":
        break