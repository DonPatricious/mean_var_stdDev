import numpy as np

def calculate(list):
    if len(list) < 9:
        raise Exception('List must contain nine numbers.')

    #convert into np array and reshape
    arr = np.array(lists).reshape(3,3)

    #create empty dictionary
    calculations = {}

    #calculate the mean
    mean_ax0 = arr.mean(axis=0).tolist()
    mean_ax1 = arr.mean(axis=1).tolist()
    mean_flat = arr.mean()
    calculations = {
        'mean' : [mean_ax0, mean_ax1, mean_flat]
    }

    #calculate variance
    var_ax0 = arr.var(axis=0).tolist()
    var_ax1 = arr.var(axis=1).tolist()
    var_flat = arr.var()
    calculations['variance'] = [var_ax0, var_ax1, var_flat]

    #calculate std
    std_ax0 = arr.std(axis=0).tolist()
    std_ax1 = arr.std(axis=1).tolist()
    std_flat = arr.std()
    calculations['standard deviation'] = [std_ax0, std_ax1, std_flat]

    #calculate max
    max_ax0 = arr.max(axis=0).tolist()
    max_ax1 = arr.max(axis=1).tolist()
    max_flat = arr.max()
    calculations['max'] = [max_ax0, max_ax1, max_flat]

    #calculate min
    min_ax0 = arr.min(axis=0).tolist()
    min_ax1 = arr.min(axis=1).tolist()
    min_flat = arr.min()
    calculations['min'] = [min_ax0, min_ax1, min_flat]

    #calculate sum
    sum_ax0 = arr.sum(axis=0).tolist()
    sum_ax1 = arr.sum(axis=1).tolist()
    sum_flat = arr.sum()
    calculations['sum'] = [sum_ax0, sum_ax1, sum_flat]



    return calculations