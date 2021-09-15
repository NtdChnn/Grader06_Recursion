def print1toN(n,goal):
    if goal >= 0:
        if goal != 0:
            print1toN(n,goal-1)
        print(bin(goal)[2:].zfill(n))
    elif goal < 0:
        print('Only Positive & Zero Number ! ! !')

n = int(input("Enter Number : "))
goal = (2**n)-1
print1toN(n,goal)
