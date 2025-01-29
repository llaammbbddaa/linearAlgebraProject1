from matplotlib import pyplot as plt

def isPrime(num):
    counter = 0
    for i in range(2, int(num / 2)):
        if (num % i == 0):
            counter += 1
    return (counter == 0)

def givePrime(lenList):
    while True:
        lenList += 1
        if (isPrime(lenList)):
            return lenList
    

def getASCII(message):
    asciiSet = []
    for i in range(len(message)):
        asciiSet.append(ord(message[i]))
    return asciiSet

def main():
    message = input("enter message (the shorter the better)\n")
    nums = getASCII(message)
    
    print(str(givePrime(len(nums))))
    
    plt.plot(nums)
    plt.ylabel("ascii values")
    plt.xlabel("each iterative value index")
    plt.show()

