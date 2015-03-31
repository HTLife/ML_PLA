#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def main():
    pair_o = [[10, 60], [20, 70]]
    pair_x = [[10, 30], [30, 10]]

    fig = plt.figure()

    ax = fig.add_subplot(111)
    #ax.margins(y=.1)
    
    x = [int(i[0]) for i in pair_o]
    y = [int(i[1]) for i in pair_o]
    ax.scatter(x, y, color='red', marker='o', s=100)

    x = [int(i[0]) for i in pair_x]
    y = [int(i[1]) for i in pair_x]
    ax.scatter(x, y, color='blue', marker='^', s=100)

    #plt.scatter(px, py)
    plt.axis([0, 100, 0, 100])
    plt.show()

if __name__ == '__main__':
    main()