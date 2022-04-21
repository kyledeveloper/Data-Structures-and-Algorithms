import generator

newlist = generator.generatorNumberList(10, 1000)
print(newlist)
#algorithms:
#1.target the first element of the list 
#2.scan the whole list and find the smallest one     
#3.swap the targeted element with the smallest one in the remaining list.
#4.target the next element of the list and repeat step 2 and 3


def selectionSort(list):
    n = len(list)
    target = 
    while (target < n - 1):
        # Reset the target at the begining of the unsorted part
        i = target
        # Reset the pointer at the beginging of the unsorted part
        pointer = target
        while (i <= n - 1):
            if list[pointer] > list[i]:
               pointer = i
            i += 1
        generator.swapl(list, target, pointer)
        target += 1
    print(list)


selectionSort(newlist)
