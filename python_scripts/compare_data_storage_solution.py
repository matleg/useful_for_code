# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 16:09:44 2014

@author: mat
compare storage in binary files by size
"""

import os
import numpy as np
import pickle

cwd = os.getcwd()

file01 = 'CV.csv'  # 1307ko   -  example of file that does not exist anymore
buffer_variable = np.loadtxt(file01, skiprows=2, delimiter=';')  # np.table


fich = open('pick', 'w')
pickle.dump(buffer_variable, fich)  # 3753ko
fich.close()

np.savetxt('savetext.out', buffer_variable)  # 4099ko

np.save('binarSave', buffer_variable)  # 1306ko
# recommended way!! loaded with np.load('file'+'npy')

buffer_variable.dump('binarDump')  # 1306ko

buffer_variable.tofile('binarToFile')  # 1306ko
# loaded with: np.fromfile('file')
