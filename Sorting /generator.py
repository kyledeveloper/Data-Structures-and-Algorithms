import random
#generate random int list with n elements and each element 
def generatorNumberList(n,max):
    unsortedList = list()
    i = 0 
    while (i <= n-1):
        randomNum = random.randint(0,max)
        unsortedList.append(randomNum)
        i+=1
    return unsortedList 

#swap the the i and i+1 element of a given list 
def swap(list, i):
    temp = list[i]
    list[i] = list[i+1]
    list[i+1] = temp
    return list

def swapl(list, level, pointer):
    temp = list[pointer]
    list[pointer] = list[level]
    list[level] = temp
    return list
vaildletter = ("","","","","","","","","","","","","","","","","","","","","","","","")

if __name__ == '__main__':
    generatorNumberList(10,100) 