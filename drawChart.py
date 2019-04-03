import matplotlib.pyplot as plt 

primeNumberList = [2]
numberList = [0,1,2]
amountOfPrimes = [0,1,2]
ratiosList = []
c = 3

def getMax():
    try:
        i = int(input("Insert Max value: "))
    except ValueError:
        print("Please insert a valid number!")
        i = getMax()
    return i

def printList(list):
    for i in list:
        print(i)
def countList(list):
    count = 1
    for i in list:
        count += 1
    return count

def main():
    c = 3
    max = 1000
    while (c <= max):
        isPrimeNumber = True
        for primeNumber in primeNumberList:
            if(c % primeNumber == 0):
                isPrimeNumber = False
        if(isPrimeNumber):
            primeNumberList.append(c)      
        numberList.append(c)
        amountOfPrimes.append(countList(primeNumberList))
        c += 1

def calcRatioList(list1, list2):
    x = 0
    for i in list1:
        try:
            ratiosList.append(list1[x]/list2[x])
        except ZeroDivisionError:
            ratiosList.append(0);
        x += 1

def tryMain():
    try:   
        main()
    except KeyboardInterrupt:
        input("\n\nInterruction detected! Press any key to continue")
        printList(primeNumberList)
        lastPrime = primeNumberList.pop()

tryMain()
plt.plot(numberList,amountOfPrimes)
plt.xlabel('Numbers') 
plt.ylabel('Primes') 
plt.title('Numbers and Primes') 
plt.show() 

calcRatioList(numberList,amountOfPrimes)
print(ratiosList)
plt.xlabel("Numbers")
plt.ylabel("Numbers/Primes")
plt.title("Numbers and Ratio")
plt.plot(numberList,ratiosList)
plt.show()