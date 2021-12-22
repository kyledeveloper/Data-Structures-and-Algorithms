
# comparison with recursion and loop
# recursion end when the base case is tought , loop end when the condition is false
# each recursion call requires extra space on the stack frame (Memory), no extra Memory being use with loop
# if we get infinite recursion, program may run out of memory and result in stack overflow
# if we get infinite loop, it loop forever since no extra memory being used
# recursion may obviously and easier to solve the problem


def factorial_recur(num):
    # base case
    if num == 0:
        return 1
        # terminates when base case is being tought 
    else: 
        # recursion case
        return num * factorial_recur(num-1)

def factorial_loop(num):
    factorial = 1
    while (num >= 1):
        factorial *= num
        num -= 1
    return factorial 
# test 
recursionSol = factorial_recur(4)
print(recursionSol)
loopSol = factorial_loop(4)
print(loopSol)
#  a way to think recurively is to found the very last step of the problem
#  also you can consider n-1 is  

def hanoi(nums,start,dest,temp):
    if nums == 1:
        print (f"move {nums} from {start} to {dest}")
        return
    hanoi(nums-1,start,temp,dest)
    print(f"move {nums} from {start} to {dest}")
    hanoi(nums-1,temp,dest,start)

hanoi(3,"a","c","b")