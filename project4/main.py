import sys
import os.path
import random

def arg_value(arg, default):
    for i in range(0, len(sys.argv)):
        if(sys.argv[i] == arg):
            try:
                argvalue = int(sys.argv[i+1])
                if(argvalue <= 0):
                    print("Invalid argument for " + arg + ", using default value " + str(default) + "!")
                    return default
            except:
                print("Invalid argument for " + arg + ", using default value " + str(default) + "!")
                return default
            return argvalue
    return default

def contains(list, obj):
    for item in list:
        if(item.lower() == obj.lower()):
            return True
    return False

wordlist = []
if(os.path.isfile("./words.txt")):
    wordlist = open('words.txt', 'r').readlines()
else:
    print("Unable find wordlist! Is words.txt in the directory?")
    exit(-1)

if(contains(sys.argv, "-h")):
    print("""
usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]
                
Generate a secure, memorable password using the XKCD method
                
optional arguments:
    -h, --help            show this help message and exit
    -w WORDS, --words WORDS
                          include WORDS words in the password (default=4)
    -c CAPS, --caps CAPS  capitalize the first letter of CAPS random words
                          (default=0)
    -n NUMBERS, --numbers NUMBERS
                          insert NUMBERS random numbers in the password
                          (default=0)
    -s SYMBOLS, --symbols SYMBOLS
                          insert SYMBOLS random symbols in the password
                          (default=0)
""")
    exit()

numwords = 4
argw = arg_value("-w", 4)
argwords = arg_value("--words", 4)
if(argw !=4 and argwords !=4):
    print("Arguments -w and --words found. Using greater of both values.")
    numwords = max(argw, argwords)
elif(argw !=4):
    numwords = argw
elif(argwords !=4):
    numwords = argwords

caps = 0
argc = arg_value("-c", 0)
argcaps = arg_value("--caps", 0)
if(argc !=0 and argcaps !=0):
    print("Arguments -c and --caps found. Using greater of both values.")
    caps = max(argc, argcaps)
elif(argc !=0):
    caps = argc
elif(argcaps !=0):
    caps = argcaps

if(caps > numwords):
    print("More capitalized words than number of words, capitalizing all words")

nums = 0
argn = arg_value("-n", 0)
argnums = arg_value("--numbers", 0)
if(argn !=0 and argnums !=0):
    print("Arguments -n and --numbers found. Using greater of both values.")
    nums = max(argn, argnums)
elif(argw !=0):
    nums = argn
elif(argnums !=0):
    nums = argnums


symbols = 0
argsy = arg_value("-s", 0)
argsymbols = arg_value("--symbols", 0)
if(argsy !=0 and argsymbols !=0):
    print("Arguments -n and --numbers found. Using greater of both values.")
    symbols = max(argsy, argsymbols)
elif(argsy !=0):
    symbols = argsy
elif(argnums !=0):
    symbols = argsymbols

symbol_list = ["~", "!", "@", "#", "$", "%", "^", "&", "*", ".", ":", ";"]

ret = ""

#generate words
for i in range(0, numwords):
    if (nums > 0 and random.randint(0, 9) < 5):
        lnums = random.randint(1, nums)
        for j in range (0, lnums):
            ret = ret + str(random.randint(0, 9))
        nums = nums - lnums
    if (symbols > 0 and random.randint(0, 9) < 5):
        lsym = random.randint(1, symbols)
        for j in range(0, lsym):
            ret = ret + symbol_list[random.randint(0, 11)]
        symbols = symbols - lsym
    word = wordlist[random.randint(0, len(wordlist)-1)].split("\n")[0]
    if(not word in ret.lower()):
        if(caps > 0 and (random.randint(0, 9)<5 or caps > (numwords-i)/2)):
            word = word.capitalize()
            caps = caps-1
        ret = ret+word
    else:
        i = i-1

for i in range(0, nums):
    ret = ret + str(random.randint(0, 9))
for i in range(0, symbols):
    ret = ret + symbol_list[random.randint(0, 11)]

print(ret)
