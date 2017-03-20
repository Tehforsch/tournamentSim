import matplotlib.pyplot as plt

def show(data, filename):
    for (title, d) in data:
        plt.plot(d[:,0], d[:,1], linewidth=2, label=title)
    plt.xlim(0, 1)
    # plt.ylim(0, 1)
    # plt.ylabel("time")
    # plt.axvline(x=0, ymin=0, ymax=1, color='k')
    # plt.axvline(x=START_POS, ymin=0, ymax=1, color='k')
    plt.legend(loc='upper left')
    # plt.show()
    plt.savefig(filename)
