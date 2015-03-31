#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def main():
    pair = [[10, 60, 1], [20, 70, 1], [10, 30, -1], [30, 10, -10]]

    fig = plt.figure()

    ax = fig.add_subplot(111)
    #ax.margins(y=.1)
    
    
    for point in pair:
        x = point[0]
        y = point[1]
        if point[2] > 0:
            ax.scatter(x, y, color='red', marker='o', s=100)
        else:
            ax.scatter(x, y, color='blue', marker='^', s=100)
    
    plt.axis([0, 100, 0, 100])
    plt.show()

if __name__ == '__main__':
    main()