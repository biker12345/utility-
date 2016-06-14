''' program to show the difference between the performance of two popular sorting algorithms ,namely
	quicksort and merge sort by providing them with a list of one million random data
'''
# modules import area
import time 
from random import randrange

billion = 1000000000
million = 1000000

#------------------------- merge sort functions  starts  ---------------------------#
def merge_sort(sequence):
    if len(sequence) < 2:
        return sequence
    m = len(sequence) // 2
    return merge(merge_sort(sequence[:m]), merge_sort(sequence[m:]))

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result

#------------------------- merge sort functions ends   ---------------------------#	


#------------------------- quick sort functions starts ---------------------------#
def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot
	
def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)

#------------------------- quick sort functions ends ---------------------------#
	
if __name__ == '__main__':
	store = []
	store2 = []
	#million random numbers are stored in the list 
	for i in range(million):
		x = randrange(1,10000)
		store.append(x)
		store2.append(x)
	# total execution time of merge sort calculated 
	start = time.time()
	merge_sort(store)
	end = time.time()
	mstime = end-start
	
	# total execution time of quick sort calculated
	start = time.time()
	quicksort(store2,0,len(store2)-1)
	end = time.time()
	qstime = end-start
	
	#result displayed 
	print('merge sort took :' + str(mstime)+'sec. \nwhich is :' + str(qstime - mstime) + 'sec. fast than that of quick sort' if mstime < qstime else 'quick sort took :' + str(qstime)+'sec.\nwhich is :' + str(mstime - qstime) + 'sec. fast than that of merge sort')
		
	


