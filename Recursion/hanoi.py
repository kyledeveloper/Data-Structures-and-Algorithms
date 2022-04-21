counter = 0
def hanoi(dish, source, helper, dest):
    global counter 
    if dish == 1:
        print(f'move {dish} from source to dest')
        counter +=1 
    else:
        hanoi(dish - 1 , source,  dest, helper)
        counter +=1 
        print( f'move {dish} form source to helper')
        hanoi(dish - 1, helper,source,dest)
hanoi(5,"a","b","c")
print(counter)