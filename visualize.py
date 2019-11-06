#visualize.py, graphs depth of .mat file, created by Anthony Androulakis, 2019
#import visualize
#visualize.depth('filename')

import mat2obj
import itertools
from matplotlib import pyplot as plt

def depth(file):
    matdict=mat2obj.loadmat(file)
    braces=''.join([char for char in str(matdict) if char in '{}'])

    num=0
    depthlist=[0]
    for i in range(0,len(braces)):
        if(braces[i]=='{'):
            num=num-1
            depthlist.append(num)
        else:
            num=num+1
            depthlist.append(num)

    plt.plot(depthlist)
    plt.show()
