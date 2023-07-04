from os import *
from sys import *
from collections import *
from math import *

def partition(arr, low, high):
    pivot = arr[high]
 
    i = low - 1
 
    for j in range(low, high):
        if arr[j] <= pivot:
 
            i = i + 1
 
            (arr[i], arr[j]) = (arr[j], arr[i])
 
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
 
    return i + 1

def quick_sort_solve(arr, low, high):
    if low < high:
 
        pi = partition(arr, low, high)
 
        quick_sort_solve(arr, low, pi - 1)
 
        quick_sort_solve(arr, pi + 1, high)
def quickSort(arr):
    # Write the function here.
    n = len(arr)
    quick_sort_solve(arr, 0, n-1)
    return arr