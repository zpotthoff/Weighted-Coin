from random import randint
from math import log
from math import pow
from math import floor
from math import ceil
import matplotlib.pyplot as plt

def fairCoin():
    # this function produces our fair coin, uniform choice of 0 or 1
    return randint(0,1)

def bogoCoin1(p):
    # this function was our original function to create a bogo coin with simple
    # p values like .25, this algo specifically only works for p = .25, .75
    # (we adjusted outcomes and could get 0, .25, .5, .75, or 1)
    coins = []
    for i in range(2):
        coins.append(fairCoin())
    if (p < .5):
        if (coins[0] == 1 and coins[1] == 1):
            return 1
        else:
            return 0
    else:
        if (coins[0] == 0 and coins[1] == 0):
            return 0
        else:
            return 1

def bogoCoin(p):
    # this function takes in a parameter p, and produces a BOGO coin
    # returning 1 with probability p and 0 with 1 - p
    numCoins = 10
    coins = []
    for i in range(numCoins):
        coins.append(fairCoin())

    cutoff = p * (pow(2, numCoins))
    total = 0
    for i in range(numCoins):
        total += coins[i] * (pow(2, i))

    if (total < cutoff):
        return 1
    else:
        return 0

def main():
    # this function produces a histogram of the different samples
    # of our desired p value, computing the average p
    p = .125
    sum = 0
    avgSum = 0
    flips = 1000
    samples = 1000
    sums = []
    for i in range(samples):
        sum = 0
        for j in range(flips):
            sum += bogoCoin(p)
        # print(sum)
        sums.append(sum/flips)
        avgSum += sum/flips
    #%matplotlib inline
    plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})

    avg = avgSum/samples
    print("p_hat is: " + str(avg))

    # Plot Histogram on x
    plt.hist(sums, bins=45)
    plt.gca().set(title='P = 0.125 Histogram', ylabel='Frequency')
    plt.axvline(p, color = 'black', linestyle = 'solid', linewidth = 5)
    plt.axvline(avg, color = 'green', linestyle = 'solid', linewidth = 2)
    plt.show()


    # print(sum)




main()
