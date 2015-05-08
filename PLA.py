#2015/03/31 15:00 Jacky Liu
import numpy as np
import random

def sign(x):
    if x <= 0:
        return -1
    return 1 

def pla(w_vector, data_x, data_y, cycleType, eta=1.0):
    flag = 0
    update_count = 0
    
    if cycleType == 'naive':
        index = range(0, len(data_x))
    elif cycleType == 'random':
        index = np.random.permutation(len(data_x))
    else:
        return

    
    while flag != 1:
        flag = 1
        for i in index:
            if sign(np.inner(w_vector, data_x[i])) != data_y[i]:
                w_vector = w_vector +  eta * data_x[i] * data_y[i]
                flag = 0
                update_count += 1

                
    return update_count
            

def main():
    data = []
    
    data = np.loadtxt('train.dat', skiprows=0)
    
    ## Add Y-intercept to first column of data_x
    data_x = np.ones((len(data),len(data[0])))
    data_x[:, 1:] = data[:, :-1 ]

    data_y = data[:, -1]

    w_vector = np.zeros(len(data_x[0]))
    
    ## HW 15 naive cycle
    #pla(w_vector, data_x, data_y, 'naive')
    
    ## HW 16 random cycle
    #count = 0.0
    #for i in range(2000):
    #    count += pla(w_vector, data_x, data_y, 'random')    
    #print(count/2000)

    ## HW 17 random cycle
    #count = 0.0
    #for i in range(2000):
    #    count += pla(w_vector, data_x, data_y, 'random', 0.5)    
    #print(count/2000)
    

if __name__ == '__main__':
    main()