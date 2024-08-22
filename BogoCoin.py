from random import randint
from math import pow
import matplotlib.pyplot as plt

class BogoCoin:
    def __init__(self, prob):
        self.prob = prob
        self.numCoins = 10

    def flip(self):
        coins = [randint(0, 1) for _ in range(self.numCoins)]

        cutoff = self.prob * (pow(2, self.numCoins))
        total = int("".join(str(x) for x in coins), 2)

        if (total < cutoff):
            return 1
        else:
            return 0