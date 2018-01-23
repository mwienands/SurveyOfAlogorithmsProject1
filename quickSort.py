#coded by michael Wienands and tyler Eggleston 
#This file is used to fill the requirements for algorithm 2
#This code writes the number of elements and the exuction time for each to a
#csv file so that you can easily visualize the expected value based off of N
import random
import timeit
import numpy
import csv


def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low , high):
 
        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:
         
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

with open('quickSortTimes.csv', 'w') as csvfile:
    fieldnames = ['numberofExuctions', 'exuctionTime']
    writer = csv.writer(csvfile, delimiter=' ')
    
    end = 0
    for i in range(10, 1000, 10): 
        arr = numpy.random.randint(i, size = (i))
        start = timeit.timeit()
              
        quickSort(arr, 0, i-1)
              
        end = timeit.timeit()
        holder = [i, "," ,end-start]
        writer.writerow(holder)

    csvfile.close()
    print("file closed")


    
      