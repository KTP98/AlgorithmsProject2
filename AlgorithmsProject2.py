


import time
import random
import sys


# Merge Sort
# code from https://www.geeksforgeeks.org/merge-sort/
# added comparison to count
def mergeSort(arr, comparisons = 0):
    
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
        
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
                comparisons += 1
            else: 
                arr[k] = R[j] 
                j+=1
                comparisons += 1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
    return arr, comparisons

# Insertion Sort 
# Code from https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
# added comparison to count
def insertion_sort(arr):
    
    comparisons = 0    
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        comparisons += 1 # have to count here as there is one comparison in the loop below even if the 
                         # the evaluation is false
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
            comparisons += 1
        # Break and do the final swap
        arr[pos] = cursor

    return arr, comparisons
    
# Bubble Sort
#code from https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
# added comparison to count
def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    comparisons = 0
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            comparisons += 1
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                    
    return arr, comparisons


sys.setrecursionlimit(10000)
# Reason for setrecersonlimit is that, python (spyder) only allows around 1000 elements
# when calling for worst case on quicksort. 

# Quick Sort
# code: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
# added comparison to count
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

# function to generate a array of random numbers
# type of array:
# d random (default) 
# s sorted  
# r reversed sorted
# m merge sort worst case
# output: array of random integers
# Time Complexity: Random O(n)  Sorted O(n log n) 

def randomArray(size, type = 'd'):
    array = []
    
    if type == 'm':
        # worst case for a merge sort is when it has to compare every element
        temp = list(range(1, size + 1)) # generate an ordered array
        odd = temp[::2] # get odd numbers 
        even = temp[1::2] # get even numbers
        odd.reverse()
        even.reverse()
        array = odd + even #combine [5, 3, 1, 6, 4, 2]
    else:
        for i in range(size):
            array.append(random.randint(1, 1000000))
    
        if type == 's':
            array = sorted(array)
        elif type == 'r':
            array = sorted(array, reverse = True)
        
    return array


# The funtion will run the algorithms using random arrays of size 100, 1000, 10,000
# and 1000000 the execution times are placed to hold the value

# The array could be: random, sorted, sorted reversed, or merge worst case
# Test could have runtimes of O(n log n) 
# Output: list exection & comparison times for each test
def testing(sortFunction, arrayType, tests = 3):
    
    length = 10^6 # the size of the array. 
    comparisons = []  
    elapsedTime = []
    for i in range(tests):
        array = randomArray(length, arrayType)
        print('\nTesiting with ' + str(length) + ' elements')
        t0 = time.perf_counter()
        _, comp = sortFunction(array)
        comparisons.append(comp)
        t1 = time.perf_counter()
        elapsedTime.append(round(t1 - t0, 5))
        print('Sort of ' + str(length) + ' elements had an elapsed time of ' + str(elapsedTime[i]) + ' with ' + str(comparisons[i]) + ' comparisons.')
        length *= 10

    return comparisons, elapsedTime

def write_file(fileName, itemsList, format="%d\n"):
    with open(fileName, 'w') as filehandle:
        filehandle.writelines(format % value for value in itemsList)


def main():
    
    print("Algorithm Testing Suite")
    print("This program will test four soring algoriths.")
    
#Merge 
    print("\n==== Merge Sort average case tests   Time Complexity Θ(n log (n)) - Sorted array ====")
    comps, elapsedTime = testing(mergeSort, 'd', 5)
    
    write_file('mergesort-avg-compares.txt', comps)
    write_file('mergesort-avg-elapsedtimes.txt', elapsedTime, "%f\n")
    
    print("\n==== Merge Sort best case tests.   Time Complexity Ω(n log (n)) - Sorted array ====")
    comps, elapsedTime = testing(mergeSort, 's')
    
    write_file('mergesort-best-compares.txt', comps)
    write_file('mergesort-best-elapsedtimes.txt', elapsedTime, "%f\n")
    
    print("\n==== Merge Sort worst case tests.   Time Complexity O(n log (n)) - merge worst arrary ====")
    comps, elapsedTime = testing(mergeSort, 'm')
    
    write_file('mergesort-worst-compares.txt', comps)
    write_file('mergesort-worst-elapsedtimes.txt', elapsedTime, "%f\n")

#Bubble
    print("\n==== Bubble Sort averge case tests.  Time Complexity Θ(n^2) - Sorted array ====")
    comps, elapsedTime = testing(bubble_sort, 'd')
    
    write_file('bublesort-avg-compares.txt', comps)
    write_file('bublesort-avg-elapsedtimes.txt', elapsedTime, "%f\n")
    
    print("\n**** Bubble Sort best case tests. - Sorted array ****")
    comps, elapsedTime = testing(bubble_sort, 's')
    
    write_file('bublesort-best-compares.txt', comps)
    write_file('bublesort-best-elapsedtimes.txt', elapsedTime, "%f\n")
    
    print("\n**** Bubble Sort worst case test. - Sorted reversed array ****")
    comps, elapsedTime = testing(bubble_sort, 'r')
    
    write_file('bublesort-worst-compares.txt', comps)
    write_file('bublesort-worst-elapsedtimes.txt', elapsedTime, "%f\n")


#Insertion
    print("\n==== Insertion Sort average case tests.   Time Complexity Θ(n^2) - Sorted arrray ====")
    comps, elapsedTime = testing(insertion_sort, 'd')
    
    write_file('insertionsort-avg-compares.txt', comps)
    write_file('insertionsort-avg-elapsedtimes.txt', elapsedTime, "%f\n")
    
    print("\n==== Insertion Sort best case tests.   Time Complexity Ω(n) - Sorted array ====")
    comps, elapsedTime = testing(insertion_sort, 's')
    
    write_file('insertionsort-best-compares.txt', comps)
    write_file('insertionsort-best-elapsedtimes.txt', elapsedTime, "%f\n")
    
    print("\n==== Insertion Sort worst case tests.   Time Complexity O(n^2) Sorted reversed array ****")
    comps, elapsedTime = testing(insertion_sort, 'r')
    
    write_file('insertionsort-worst-compares.txt', comps)
    write_file('insertionsort-worst-elapsedtimes.txt', elapsedTime, "%f\n")

#Quick
    print("\n==== Quick Sort average case test.   Time Complexity Ω(n log (n)) - Sorted array ====")
    comps, elapsedTime = testing(quick_sort, 'd', 5)
    
    write_file('quicksort-avg-compares.txt', comps)
    write_file('quicksort-avg-elapsedtimes.txt', elapsedTime, "%f\n")
    
    print("\n==== Quick Sort best case tests.   Time Complexity Θ(n log (n)) - Sorted array ====")
    comps, elapsedTime = testing(quick_sort, 'r')
    
    write_file('quicksort-best-compares.txt', comps)
    write_file('quicksort-best-elapsedtimes.txt', elapsedTime, "%f\n")

    print('\n==== Quick Sort worst case tests.    Time Complexity O(n^2) Sorted reversed array - Sorted array ====')
    comps, elapsedTime = testing(quick_sort, 's')
   
    write_file('quicksort-worst-compares.txt', comps)
    write_file('quicksort-worst-elapsedtimes.txt', elapsedTime, "%f\n")
    
if __name__ == "__main__":
    main()



# https://stackoverflow.com/questions/27116255/python-quicksort-maximum-recursion-depth
# source for quick sort maxing out at 3 average cases and no worst case (or 3 cases when testing worst case)
