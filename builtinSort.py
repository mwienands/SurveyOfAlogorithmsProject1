#coded by michael Wienands and tyler Eggleston 
#This file is used to fill the requirements for algorithm 3
#This code writes the number of elements and the exuction time for each to a
#csv file so that you can easily visualize the expected value based off of N
import random
import timeit
import numpy
import csv

with open('biultInSortTimes.csv', 'w') as csvfile:
    fieldnames = ['numberofExuctions', 'exuctionTime']
    writer = csv.writer(csvfile, delimiter=' ')
    
    end = 0
    for i in range(10, 1000, 10): 
        arr = numpy.random.randint(i, size = (i))
        start = timeit.timeit()
        arr.sort()
            
        end = timeit.timeit()
        holder = [i, "," ,end-start]
        writer.writerow(holder)

    csvfile.close()
    print("file closed")


    
      