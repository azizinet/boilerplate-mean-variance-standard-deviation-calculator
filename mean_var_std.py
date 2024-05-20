import numpy as np

def calculate(list):
    if np.size(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        nplist = np.array(list)
        new_matrix = np.reshape(list, (3,3))
        calculations = {}
        
        calculations['mean'] = [[i for i in np.mean(new_matrix, axis = 0)], [i for i in np.mean(new_matrix, axis = 1)], float(np.mean(new_matrix))]
        calculations['variance'] = [[i for i in np.var(new_matrix, axis = 0)], [i for i in np.var(new_matrix, axis = 1)], float(np.var(new_matrix))]
        calculations['standard deviation'] = [[i for i in np.std(new_matrix, axis = 0)], [i for i in np.std(new_matrix, axis = 1)], float(np.std(new_matrix))]
        calculations['max'] = [[i for i in np.max(new_matrix, axis = 0)], [i for i in np.max(new_matrix, axis = 1)], np.max(new_matrix)]
        calculations['min'] = [[i for i in np.min(new_matrix, axis = 0)], [i for i in np.min(new_matrix, axis = 1)], np.min(new_matrix)]
        calculations['sum'] = [[i for i in np.sum(new_matrix, axis = 0)], [i for i in np.sum(new_matrix, axis = 1)], np.sum(new_matrix)]

        return calculations