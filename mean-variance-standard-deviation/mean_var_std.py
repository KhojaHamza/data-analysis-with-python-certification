import sys
import numpy as np
def calculate(list_):
    if len(list_) != 9:
        raise ValueError("List must contain nine numbers.")
    matrice_ = np.array(list_).reshape((3,3))
    
    mean = [matrice_.mean(axis=0).tolist(),matrice_.mean(axis=1).tolist(),float(matrice_.mean())]
    variance =[matrice_.var(axis=0).tolist(),matrice_.var(axis=1).tolist(),float(matrice_.var())]
    std_ =[matrice_.std(axis=0).tolist(),matrice_.std(axis=1).tolist(),float(matrice_.std())]
    max_ = [matrice_.max(axis=0).tolist(),matrice_.max(axis=1).tolist(),int(matrice_.max())]
    min_=[matrice_.min(axis=0).tolist(),matrice_.min(axis=1).tolist(),int(matrice_.min())]
    sum_=[matrice_.sum(axis=0).tolist(),matrice_.sum(axis=1).tolist(),int(matrice_.sum())]
    
    return {'mean':mean,
  'variance': variance,
  'standard deviation':std_,
  'max': max_,
  'min': min_,
  'sum': sum_}