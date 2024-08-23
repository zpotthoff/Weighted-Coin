import matplotlib.pyplot as plt
from BogoCoin import BogoCoin
from statistics import mean

def main():
    # this function produces a histogram of the different samples
    # of our desired p value, computing the average p
    probability = 0.125
    wCoin = BogoCoin(probability)
    flips = 1000
    samples = 1000
    sums = []
    for i in range(samples):
        heads = 0
        for j in range(flips):
            heads += wCoin.flip()
        sums.append(heads/flips)
    plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})

    avg = mean(sums)
    print("p_hat is: " + str(avg))

    # Plot Histogram on x
    plt.hist(sums, bins=30)
    plt.gca().set(title='P = 0.125 Histogram', ylabel='Frequency')
    plt.axvline(probability, color = 'black', linestyle = 'solid', linewidth = 2, label = 'p = 0.125')
    plt.axvline(avg, color = 'red', linestyle = 'solid', linewidth = 2, label = 'p_hat = ' + str(avg))
    plt.legend()
    plt.show()

main()
