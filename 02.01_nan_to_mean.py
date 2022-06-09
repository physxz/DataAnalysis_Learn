from ast import main
from tkinter import mainloop
from tkinter.tix import MAIN


import numpy as np

def fill_ndarray(t1):
    for i in range(t1.shape[1]):
        cur_col = t1[:,i] # 先定位某一列
        nan_num = np.count_nonzero(cur_col != cur_col) # 判断当前列是否含有nan
        if nan_num != 0: # 先定位到有nan的列(不用每列都查找替换nan，提高效率)
            cur_not_nan_col = cur_col[cur_col == cur_col] # 然后刨除掉nan列中的nan，只留正常值
            cur_col[np.isnan(cur_col)] = cur_not_nan_col.mean()
    return t1


if __name__ == '__main__':
    t1 = np.arange(12).reshape((3,4)).astype('float')
    t1[1,2:] = np.nan
    print(t1)
    print('*'*20)
    t1 = fill_ndarray(t1)
    print(t1)