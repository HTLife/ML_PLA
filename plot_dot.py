#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

import math#for test

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
    
    #plt.plot([0, 20], [90, 200], 'k-')
    #x = np.linspace(0, 3, 100)

    x2 = [1, 2, 4, 6, 8]
    y2 = [2, 4, 8, 12, 16]
 
    
    plt.plot(x2, y2, 'g')
        #plt.plot([0, 1, 10], 'k-')
    
    #line_x = np.linspace(-15,15,100)
    #line_y = line_x * 3
    #ax.plot(x,y)
    
    ax.axis([0, 100, 0, 100])
    #plt.show()
    plt.savefig('foo.png')

if __name__ == '__main__':
    main()