# convert inputted string to ascii list
# convert ascii list to set of points on a graph

from matplotlib import pyplot as plt
import numpy as np
    
def generateFunction(lenList, func_str):
    x = np.linspace(0, lenList, 100)  # 100 points for smooth plotting
    
    # Convert function string into a callable function
    y = [eval(func_str.replace("x", str(val))) for val in x]
    
    fig = plt.figure(figsize=(12, 7))
    plt.plot(x, y, alpha=0.4)
    
    return plt
    

def generateMiniFunction(lenList, ignore, asciiList):
    func = "(("
    
    for j in range(lenList):
        if j is not ignore:
            func += "(x - " + str(j) + ") * "
    
    func = func.rstrip(" * ")  # Remove trailing " * " at the end
    func += ")"  # Close the parentheses properly
    
    func += " / ("
    for i in range(lenList):
        if i is not ignore:
            func += "(" + str(ignore) + " - " + str(i) + ") * "
    
    func = func.rstrip(" * ")  # Remove trailing " * " at the end
    func += "))"  # Close the parentheses properly
    
    func = "(" + str(asciiList[ignore]) + " * " + func + ")"
    
    #print("mini func >> " + func)
    return func

def generateFullFunction(lenList, asciiList):
    fullFunc = "("
    for i in range(lenList):
        if (i < (lenList - 1)):
            fullFunc += (generateMiniFunction(lenList, i, asciiList) + " + ")
        else:
            fullFunc += (generateMiniFunction(lenList, i, asciiList) + ")")
    #print(fullFunc)
    return fullFunc

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

def addPoints(num, nums):
    temp = generateFullFunction(len(nums), nums)
    temp = temp.replace("x", str(num))
    
    return evaluateAt(temp)

def evaluateAt(nums):
    return int(eval(nums))

def main():
    message = input("enter message (the longer the better)\n")
    nums = getASCII(message)
    
    #print(str(givePrime(len(nums))))
    
    #print(generateFullFunction(len(nums), nums))
    plt = generateFunction(len(nums), generateFullFunction(len(nums), nums))
    plt.plot(nums)
    plt.ylabel("ascii values")
    plt.xlabel("each iterative value index")
    
    quant = input("how many extra points do you want? >> ")
    for i in range(len(nums), len(nums) + int(quant)):
        nums.append(addPoints(i, nums))
    #plt.plot(nums)
        
    print(nums)
    plt.show()

main()
            

