''' program to show multithreading in which one thread performs selection sort and other quick sort 
	selection sort thread starts first but is forced to sleep for 3 sec meanwhile quick sort thread 
	starts and finishes its work
'''

#import of multiprocessing module (used for multithreading in python )
import multiprocessing
import time 

#----------------------- quick sort function starts --------------------#
def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot
	
def quicksort(array, begin, end):
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)

#----------------------------------------quick sort finished--------------#

#-----------------------------selectionSort function starts---------------#	
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
#-----------------------------selectionSort function ends---------------#

#-----------------------------Driver functions starts-------------------#	   
def selectionsortDriver(array):
	print('\nselection sort starts')
	print('\nselection sort goes for sleep')
	time.sleep(3)
	print('\nselection sort wakes up')
	selectionSort(array)
	print('\nselection sort:'+ str(array))
	print('\nselection sort finished')

def quicksortDriver(array):
	print('\nquick sort starts ')
	quicksort(array,0,len(array)-1)
	print('\nquick sort:'+str(array))
	print ('\nquick sort Finished')

#-----------------------------Driver functiona ends--------------------#	
	
if   __name__ == '__main__':
	store  = [56,76,89,87,67,55,1,3,34,99,199]
	store2  = [58,74,81,96,67,55,11,34,340,199,99]
	p = multiprocessing.Process(target = selectionsortDriver,args = (store,))
	q = multiprocessing.Process(target = quicksortDriver , args = (store2,))
	p.start()
	q.start()