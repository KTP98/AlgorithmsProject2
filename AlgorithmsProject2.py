import sys
sys.setrecursionlimit(100000)
import time
import random

# https://medium.com/@george.seif94/a-tour-of-the-top-5- sorting-algorithms-with-python-code-43ea9aa02889.
def partition(array, begin, end, comparisons):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        comparisons += 1
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx, comparisons

def quick_sort_recursion(array, begin, end):
    comparisons = 0
    if begin < end:
        pivot_idx, comparisons = partition(array, begin, end, comparisons)
        comparisons += quick_sort_recursion(array, begin, pivot_idx-1)
        comparisons += quick_sort_recursion(array, pivot_idx+1, end)
    return comparisons

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    return 0, quick_sort_recursion(array, begin, end)
