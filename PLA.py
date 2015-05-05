#2015/03/31 15:00 Jacky Liu
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

def plot(w_vector, data_x, data_y, name):    
    fig = plt.figure()

    ax = fig.add_subplot(111)
    ax.axis([-0, 1, -0, 1])
    #ax.margins(y=.1)
    
    
    for i in range(0, len(data_x)):
        x = data_x[i][0]
        y = data_x[i][1]
        if data_y[i] >= 0:
            ax.scatter(x, y, color='red', marker='o', s=100)
        else:
            ax.scatter(x, y, color='blue', marker='^', s=100)
    
    
    line_x = [-10, 100]
    line_y = []
    threshold = w_vector[0]
    
    for x_tmp in line_x:
        try:
            line_y.append(((-1)*threshold - w_vector[1]*x_tmp) / float(w_vector[2]))
        except:
            line_y.append(0)
    #print(str(line_x) + str(line_y))
    #plt.plot(line_p1, line_p2, 'k-')

    plot_result = plt.plot(line_x, line_y, 'k-')
    plt.title('step ' + name)
    
    
    #plt.show()
    plt.savefig(name + '.png')
    
    return plot_result
    

def h(w_vector, data_x):
    if np.dot(w_vector[1:], data_x) + w_vector[0] > 0:
        return 1
    else:
        return -1

def update_w_vector(w_vector, data_x, data_y):
    for i in range(0, len(data_x)):
        w_vector[i+1] += data_x[i]*data_y
       
    

def pla(w_vector, data_x, data_y):
    flag = 0
    update_count = 1
    while flag != 1:
        flag = 1
        for i in range(0, len(data_x)):
            if h(w_vector, data_x[i]) != data_y[i]:
                #print(str(update_count) + ' update')
                update_w_vector(w_vector, data_x[i], data_y[i])
                #print('\t' + str(w_vector))
                flag = 0
                #plot(w_vector, data_x, data_y, '{0:02d}'.format(update_count))
                update_count += 1
                
    print('Update count = ' + str(update_count))
            

def main():
    data = []
    
    f = open("train.dat", "r")
    for line in f:
        floats = [float(x) for x in line.split()]
        data.append(floats)
    
    
    #data = [[10, 60, 1], [20, 70, 1], [10, 30, -1], [30, 10, -1]]
    #data = [[10, 60, 1], [20, 70, 1], [60, 30, -1], [30, 10, -1]]
    data_x = [i[:4] for i in data]
    data_y = [i[-1] for i in data]
    print('Data point:' + str(data_x[0]))
    print('Type:' + str(data_y[0]))
    
    w_vector = [-1, 0, 0, 0, 0]
    
    pla(w_vector, data_x, data_y)
    
    print(w_vector)
    
    

if __name__ == '__main__':
    main()