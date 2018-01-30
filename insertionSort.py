def insertSort(array):
    for i in range(len(array)):
        j=i-1
        value=array[i]
        while j>=0 and value<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1]=value

if __name__=="__main__":
    array1=[54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertSort(array1)  
    print(array1)
