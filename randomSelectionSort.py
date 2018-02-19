import random
import timeit
import numpy
import csv

 
            
def selectionSort(arr, k):   
    aL =[] #sub array for all less than index
    aE =[] #sub array for all equel tp index
    aG =[] #sub array for all greater than index     
    n = random.randint(0, len(arr)) #random value between o, length(arr)
    print 'n' ,n
    try:
        for i in arr.flat:
            if (arr[i] < n):
                aL.append(arr[i])
            elif(arr[i] > n):
                aG.append(arr[i])
            else:
                aE.append(arr[i])
    except:
        for i in range(0, len(arr)):
            if (arr[i] < n):
                aL.append(arr[i])
            elif(arr[i] > n):
                aG.append(arr[i])
            else:
                aE.append(arr[i])      
    print("aL", aL)
    
    print("aE", aE)
   
    print("aG", aG)
    
    
    if (k < len(aL)):
        
        return selectionSort(aL, k)
    elif (k<=len(aL) + len(aE)):
        return n
    else:
        return selectionSort(aG, k- (len(aL)  + len(aE)))
        
with open('selectionSortTimes.csv', 'w') as csvfile:
    
    fieldnames = ['numberofExuctions', 'exuctionTime']
    writer = csv.writer(csvfile, delimiter=' ')
    
    end = 0
    #for i in range(10, 100, 10): 
    
    
    arr = numpy.random.randint(10, size = (15))
    print arr

    k = random.randint(1,15)
    print k
    start = timeit.timeit()
          
    print(selectionSort(arr, k))
          
    end = timeit.timeit()
    holder = [10, "," ,end-start]
    writer.writerow(holder)

    csvfile.close()
    print("file closed")


