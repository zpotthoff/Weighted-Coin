from random import randint
from math import log
from math import pow
from math import floor
from math import ceil
import matplotlib.pyplot as plt

class BogoCoin:
    def __init__(self, prob):
        self.prob = prob
        self.numCoins = 10

    def flip(self):
        coins = []
        for i in range(self.numCoins):
            coins.append(randint(0, 1))

        cutoff = self.prob * (pow(2, self.numCoins))
        total = 0
        for i in range(numCoins):
            total += coins[i] * (pow(2, i))

        if (total < cutoff):
            return 1
        else:
            return 0
