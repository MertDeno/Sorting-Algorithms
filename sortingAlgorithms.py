#from time import timeit

def insertionSort(array):
    for i in range(len(array)):
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key

    print(array)

def selectionSort(array):
    for i in range(len(array)):
        minimum=i
        for j in range(len(array)-1):
            if array[j]<minimum:
                minimum=array[j]

            array[i],array[minimum]=array[minimum],array[i]

    print(array)

def partition(array,low,high):

    pivotNum=array[high]
    i=low-1
    
    for j in range(low,high):
        if pivotNum >= array[j]:
            i+=1
            array[i],array[j]=array[j],array[i]

    array[i+1],array[high]=array[high],array[i+1]
    return i+1

def quickSort(array,low,high):
    if low < high:
        q=partition(array,low,high)
        quickSort(array,low,q-1)
        quickSort(array,q+1,high)

def heapifyArr(array,n,i):
    largest=i
    left=2*i+1
    right=2*i+2

    if left<n and array[left]>array[largest]:
        largest=left

    if right<n and array[right]>array[largest]:
        largest=right

    if largest!=i:
        array[i],array[largest]=array[largest],array[i]

        heapifyArr(array,n,largest)

def sortArray(array):
    x=len(array)

    for i in range(x,-1,-1):
        heapifyArr(array,x,i)

    for i in range(x-1,0,-1):
        array[0],array[i]=array[i],array[0]
        heapifyArr(array,i,0)

def merge(array1):
    if len(array1)>1:
        mid=len(array1)//2
        leftSide=array1[:mid]
        rightSide=array1[mid:]

        merge(leftSide)
        merge(rightSide)

        i=0
        j=0
        k=0

        while i < len(leftSide) and j < len(rightSide):
            if leftSide[i] < rightSide[j]:
                array1[k]=leftSide[i]
                i=i+1
            else:
                array1[k]=rightSide[j]
                j=j+1
            k=k+1

        while i < len(leftSide):
            array1[k]=leftSide[i]
            i=i+1
            k=k+1

        while j < len(rightSide):
            array1[k]=rightSide[j]
            j=j+1
            k=k+1


def countSort(alist,maxval):
    n=len(alist)
    m=maxval+1
    eleOfList=[0]*m

    for i in alist:
        eleOfList[i]+=1

    i=0
    for x in range(m):
        for j in range(eleOfList[x]):
             alist[i]=x
             i+=1    
    return alist

if __name__=="__main__":
    array=[33,44,21,83,75]
    array1=[54, 26, 93, 17, 77, 31, 44, 55, 20]
    array2=[1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1]
    
    print("Insertion Sort")
    insertionSort(array)
    
    print("Selection Sort")
    selectionSort(array)

    print("Quick Sort")
    high=len(array)   
    quickSort(array,0,high-1)
    for i in range(high):
        print("%d "%array[i])

    print("Heap Sort")
    sortArray(array1)
    for i in range(len(array1)):
        print("%d "%array1[i])

    print("Merge Sort")
    merge(array1)
    print(array1)

    
    print("Count Sort")
    print(countSort(array2,7))
