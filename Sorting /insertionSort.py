



import generator

unsortlist = generator.generatorNumberList(5,100)
print(unsortlist)

def insertionSort(unsortlist):
    for i in range(1,len(unsortlist)):
        temp = unsortlist[i]
        j = i - 1
        while(j >=0 and temp < unsortlist[j]):
            unsortlist[j+1] =  unsortlist[j]
            j -= 1
        unsortlist[j+1] = temp
    print(unsortlist)
insertionSort(unsortlist)
