# in this encryption project, we will create a function that encrypts strings (without numbers, e.g. useful for names).

# import random for random numbers
import random
import math

allLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ä", "ö", "ü","0","1","2","3","4","5","6","7","8","9","_",".",",","(",")",":",";","-"]

def encrypt(name):
    if (type(name) is str and len(name) > 0):
        # randomly generate the parameters and powers for the function that will generate the encrypted string
        a = random.randint(0, 10) # used to be len(allLetters) - 1
        b = random.randint(0, 10)
        c = random.randint(0, 10)

        # convert name into a lowercased list
        lowerName = name.lower()
        letterList = list(lowerName)
        encryptedLetterList = []

        for i in range(len(letterList)):
            #if there is a space, we change it to an underscore
            if letterList[i] == " ":
                letterToEncrypt = "_"
            else:
                letterToEncrypt = letterList[i]
            # find out, where in the alphabet the letter is
            x = allLetters.index(letterToEncrypt)
            # find the index of the encrypted letter via our random function
            newLetterIndex = ((a * x) + (b * x) + (c * x)) % len(allLetters)
            # also save the quotient for each letter (necessary for decryption)
            letterQuotient = math.floor(((a * x) + (b * x) + (c * x)) / len(allLetters))
            # add the two letters (encrypted letter & quotient)
            encryptedLetterList.append(allLetters[newLetterIndex])
            encryptedLetterList.append(allLetters[letterQuotient])

        # make it uppercase
        encryptedLetterList[0] = encryptedLetterList[0].upper()

        # add the parameters a to c as information into the string
        encryptedLetterList.append(allLetters[a])
        encryptedLetterList.append(allLetters[b])
        encryptedLetterList.append(allLetters[c])

        encryptedString = ""
        # make a string out of the list
        for i in range(len(encryptedLetterList)):
            encryptedString += encryptedLetterList[i]

        print("Encrypted word:", encryptedString)
        return
    print("Please enter a real word to encrypt.")



def decrypt(encryptedName):
    if (type(encryptedName) is str and len(encryptedName) > 0):
        lowerEncryptedName = encryptedName.lower()
        encryptedLetterList = list(lowerEncryptedName)
        realLetterList = []
        # get the values for a, b, and c
        a = allLetters.index(encryptedLetterList[-3])
        b = allLetters.index(encryptedLetterList[-2])
        c = allLetters.index(encryptedLetterList[-1])
        # only get the letters of the name and the quotients of each letter
        for i in range(math.ceil((len(encryptedLetterList) - 3) / 2)):
            # print(encryptedLetterList[i * 2], encryptedLetterList[i * 2 + 1])
            # calculating the quotient times the divisor plus the rest to get the former total
            total = allLetters.index(encryptedLetterList[i * 2 + 1]) * len(allLetters) + allLetters.index(encryptedLetterList[i * 2])
            # calculate x out of the given figures:
            # ax + bx + cx = total
            # x(a + b + c) = total
            # x = total / (a + b + c)
            x = int(total / (a + b + c))
            # add the correct letters to a list
            realLetterList.append(allLetters[x])

        # make the first letter uppercase
        realLetterList[0] = realLetterList[0].upper()

        realWord = ""
        # make a string out of the list
        for i in range(len(realLetterList)):
            realWord += realLetterList[i]
        
        print("Decrypted word:", realWord)
        return
    print("Please enter a real encrypted term to decrypt.")


encrypt(input("Please enter the term you want to encrypt: "))
