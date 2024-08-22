import matplotlib.pyplot as plt
from BogoCoin import BogoCoin

def main():
    # this function produces a histogram of the different samples
    # of our desired p value, computing the average p
    wCoin = BogoCoin(0.125)
    sum = 0
    avgSum = 0
    flips = 1000
    samples = 1000
    sums = []
    for i in range(samples):
        sum = 0
        for j in range(flips):
            sum += wCoin.flip()
        # print(sum)
        sums.append(sum/flips)
        avgSum += sum/flips
    plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})

    avg = avgSum/samples
    print("p_hat is: " + str(avg))

    # Plot Histogram on x
    plt.hist(sums, bins=45)
    plt.gca().set(title='P = 0.125 Histogram', ylabel='Frequency')
    plt.axvline(0.125, color = 'black', linestyle = 'solid', linewidth = 2)
    plt.axvline(avg, color = 'red', linestyle = 'solid', linewidth = 2)
    plt.show()

main()
