#Original 
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

#Quick sort
# modified to get number of comparisons
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
# Appently in the return statment above quicksort will return the empty array 
# as well so in order to avoid this return had to have a 0 after it.


#insertion sort function
#code: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
# modified to get number of comparisons
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


#bubble sort 
#code: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
# modified to get number of comparisons
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

# Merge sort
# https://www.geeksforgeeks.org/merge-sort/
# modified to get number of comparisons
def mergeSort(arr, comparisons = 0):
    
    if len(arr) >1: 
        #Finding the mid of the array 
        mid = len(arr)//2 
        # Divide array elements 
        L = arr[:mid] 
        # into 2 halves 
        R = arr[mid:] 
  
        # Sorting first half 
        mergeSort(L) 
        # Sorting second half
        mergeSort(R) 
        
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

def randomArray(size, type = 'd'):
    array = []
    if type == 'm':
        temp = list(range(1, size + 1)) 
        odd = temp[::2] 
        even = temp[1::2] 
        odd.reverse()
        even.reverse()
        array = odd + even 
    else:
        for i in range(size):
            array.append(random.randint(1, 1000000))
        if type == 's':
            array = sorted(array)
        elif type == 'r':
            array = sorted(array, reverse = True)
        
    return array


def testTime(sortFunction, arrayType, tests = 3):
    arrsize = 100  # size of the array
    comparisons = []  #  number of comparisons per run
    elapsedTime = []  # elapsed time per run
    for i in range(tests):
        array = randomArray(arrsize, arrayType)
        print('\nTesiting with ' + str(arrsize) + ' elements')
        t0 = time.perf_counter()
        _, comp = sortFunction(array)
        comparisons.append(comp)
        t1 = time.perf_counter()
        elapsedTime.append(round(t1 - t0, 5))
        print('Sorting of ' + str(arrsize) + ' elements had an elapsed time of ' + str(elapsedTime[i]) + 's, with ' + str(comparisons[i]) + ' comparisons.')
        arrsize *= 10

    return comparisons, elapsedTime

def writeFile(fileName, itemsList, format="%d\n"):
    with open(fileName, 'w') as filehandle:
        filehandle.writelines(format % value for value in itemsList)

def main():
    
    print("\n**** QUICK-SORT BEST RUN TIME ****")
    comps, elapsedTime = testTime(quick_sort, 'd', 5)
    
    writeFile('quicksort-avg-compares.txt', comps)
    writeFile('quicksort-avg-elapsedtimes.txt', elapsedTime, "%f\n")

    print('\n**** QUICK-SORT WORST RUN TIME - Sorted array ****')
    comps, elapsedTime = testTime(quick_sort, 's')
   
    writeFile('quicksort-worst-compares.txt', comps)
    writeFile('quicksort-worst-elapsedtimes.txt', elapsedTime, "%f\n")
    
    print("\n**** MERGE-SORT AVERAGE RUN TIME ****")
    comps, elapsedTime = testTime(mergeSort, 'd', 5)
    
    writeFile('mergesort-avg-compares.txt', comps)
    writeFile('mergesort-avg-elapsedtimes.txt', elapsedTime, "%f\n")
    
    print("\n**** MERGE-SORT BEST RUN TIME ****")
    comps, elapsedTime = testTime(mergeSort, 's', 5)
    
    writeFile('mergesort-best-compares.txt', comps)
    writeFile('mergesort-best-elapsedtimes.txt', elapsedTime, "%f\n")
    
    print("\n**** MERGE-SORT WORST RUN TIME ****")
    comps, elapsedTime = testTime(mergeSort, 'm', 5)
    
    writeFile('mergesort-worst-compares.txt', comps)
    writeFile('mergesort-worst-elapsedtimes.txt', elapsedTime, "%f\n")

if __name__ == "__main__":
        main()

        
#Updated 10/13/21 4:46 pm       
        
import time
import random
import sys
sys.setrecursionlimit(10000)

# https://www.geeksforgeeks.org/merge-sort/
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

# https://medium.com/@george.seif94/a-tour-of-the-top-5- sorting-algorithms-with-python-code-43ea9aa02889.
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

# https://medium.com/@george.seif94/a-tour-of-the-top-5- sorting-algorithms-with-python-code-43ea9aa02889.
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


def randomArray(size, type = 'd'):
    array = []
    
    if type == 'm':
        # worst case for a merge sort is to make the algorithm compare every element
        temp = list(range(1, size + 1)) # generate an ordered sequence [1, 2, 3, 4, 5, 6]
        odd = temp[::2] # get the odd numbers [1, 3, 5]
        even = temp[1::2] # get the even numbers [2, 4, 6]
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

def testRunner(sortFunction, arrayType, tests = 3):
    
    mag = 100  # the size of the array. First execution the size is 100
    comparisons = []  # list holding the number of comparisons per run
    elapsedTime = []  # list holding the elapsed time per run
    for i in range(tests):
        array = randomArray(mag, arrayType)
        print('\nTesiting with ' + str(mag) + ' elements')
        t0 = time.perf_counter()
        # ignoring the array with _
        _, comp = sortFunction(array)
        comparisons.append(comp)
        t1 = time.perf_counter()
        elapsedTime.append(round(t1 - t0, 5))
        print('Sort of ' + str(mag) + ' elements had an elapsed time of ' + str(elapsedTime[i]) + ' with ' + str(comparisons[i]) + ' comparisons.')
        mag *= 10

    return comparisons, elapsedTime

def writeFile(fileName, itemsList, format="%d\n"):
    with open(fileName, 'w') as filehandle:
        filehandle.writelines(format % value for value in itemsList)


def main():
    
    print("Algorithm Test Suite")
    print("This program will test four soring algorithms. Two have a time complexit of O(n^2)")
    print("and two have time complext of O(n log n)")
    
    print("\n**** Merge Sort average case tests ****")
    comps, elapsedTime = testRunner(mergeSort, 'd', 5)
    
    writeFile('mergesort-avg-compares.txt', comps)
    writeFile('mergesort-avg-elapsedtimes.txt', elapsedTime, "%f\n")
    
    print("\n**** Merge Sort best case tests ****")
    comps, elapsedTime = testRunner(mergeSort, 's', 5)
    
    writeFile('mergesort-best-compares.txt', comps)
    writeFile('mergesort-best-elapsedtimes.txt', elapsedTime, "%f\n")
    
    print("\n---- Merge Sort worst case tests ----")
    comps, elapsedTime = testRunner(mergeSort, 'm', 5)
    
    writeFile('mergesort-worst-compares.txt', comps)
    writeFile('mergesort-worst-elapsedtimes.txt', elapsedTime, "%f\n")
    
    print("\n---- Insertion Sort average case tests. ----")
    comps, elapsedTime = testRunner(insertion_sort, 'd')
    
    writeFile('insertionsort-avg-compares.txt', comps)
    writeFile('insertionsort-avg-elapsedtimes.txt', elapsedTime, "%f\n")
    
    print("\n---- Insertion Sort best case tests. - Sorted array ----")
    comps, elapsedTime = testRunner(insertion_sort, 's')
    
    writeFile('insertionsort-best-compares.txt', comps)
    writeFile('insertionsort-best-elapsedtimes.txt', elapsedTime, "%f\n")
    
    print("\n---- Insertion Sort worst case tests. - Sorted reversed array ----")
    comps, elapsedTime = testRunner(insertion_sort, 'r')
    
    writeFile('insertionsort-worst-compares.txt', comps)
    writeFile('insertionsort-worst-elapsedtimes.txt', elapsedTime, "%f\n")

    print("\n---- Bubble Sort averge case tests. ----")
    comps, elapsedTime = testRunner(bubble_sort, 'd')
    
    writeFile('bublesort-avg-compares.txt', comps)
    writeFile('bublesort-avg-elapsedtimes.txt', elapsedTime, "%f\n")
    
    print("\n---- Bubble Sort best case tests. - Sorted array ----")
    comps, elapsedTime = testRunner(bubble_sort, 's')
    
    writeFile('bublesort-best-compares.txt', comps)
    writeFile('bublesort-best-elapsedtimes.txt', elapsedTime, "%f\n")
    
    print("\n---- Bubble Sort worst case test. - Sorted reversed array ----")
    comps, elapsedTime = testRunner(bubble_sort, 'r')
    
    writeFile('bublesort-worst-compares.txt', comps)
    writeFile('bublesort-worst-elapsedtimes.txt', elapsedTime, "%f\n")

    print("\n---- Quick Sort best case test ----")
    comps, elapsedTime = testRunner(quick_sort, 'd', 5)
    
    writeFile('quicksort-avg-compares.txt', comps)
    writeFile('quicksort-avg-elapsedtimes.txt', elapsedTime, "%f\n")

    print('\n---- Quick Sort worst case tests - Sorted array ----')
    comps, elapsedTime = testRunner(quick_sort, 's')
   
    writeFile('quicksort-worst-compares.txt', comps)
    writeFile('quicksort-worst-elapsedtimes.txt', elapsedTime, "%f\n")
    
if __name__ == "__main__":
    main()
        
