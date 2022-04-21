import generator
newlist = generator.generatorNumberList(10,500)
print(newlist)
def bubSort(list):
    # count how many elements the list has 
    n = len(list)
    while True:
        # reset the isSwapped, and uncomment the statement with * at the end.
        isSwapped = False
        # start the second loop at i = 0 every time when second loop is finished. Which means start in the beginning 
        i = 0
        while( i < n-1):
            # if the left side is greater than right side, swap those two number 
            if list[i] > list[i+1]: # change the greater sign to less than sign, can change to order from ascending to descending 
                generator.swap(list,i)
                # toggle if swaped 
                isSwapped = True
            #increment the i and loop again
            i +=1
        # according to this algorithms, the last element of the list shoule be the greatest one, so we can start the second loop with n = n-1 
        n -=1
        # if we do not swap in the second loop, it means the list are sorted. then we can break the loop
        if isSwapped == False:
           break     
    return list     

print(bubSort(newlist))

