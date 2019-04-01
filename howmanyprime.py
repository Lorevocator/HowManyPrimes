primeNumberList = [2]
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
    count = 0
    for i in list:
        count += 1
    return count
def main():
    c = 3
    max = getMax()
    while (c <= max):
        isPrimeNumber = True
        for primeNumber in primeNumberList:
            if(c % primeNumber == 0):
                isPrimeNumber = False
        if(isPrimeNumber):
            primeNumberList.append(c)
        #print(c)
        c +=1
    #printList(primeNumberList)
    print("\n\n\n","Da 0 a ",c-1," ci sono ",countList(primeNumberList)," numeri primi")
    calcRatio(c-1,countList(primeNumberList))

def tryMain():
    try:   
        main()
    except KeyboardInterrupt:
        input("\n\nInterruction detected! Press any key to continue")
        printList(primeNumberList)
        lastPrime = primeNumberList.pop()
        print("","Da 0 a ",lastPrime," ci sono ",countList(primeNumberList)," numeri primi")
        calcRatio(lastPrime,countList(primeNumberList))

def calcRatio(numbers, numberOfPrimes):
    ratio = numberOfPrimes/numbers
    print("The ratio is ",ratio)

tryMain()
#while input("Do you wish to continue?").lower() == "y":
while True:
    primeNumberList.clear()
    primeNumberList = [2]
    tryMain()