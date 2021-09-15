countUp = 1;
countDown = 0;
def staircase(n):
    global countUp,countDown
    showUS = '___________________________________________________'
    showNS = '###################################################'
    if n > 0:
        print(f'{showUS[:n-1]}{showNS[:countUp]}')
        countUp += 1
        if n != 1:
            staircase(n - 1)
    elif n < 0:
        print(f'{showUS[:countDown]}{showNS[:n*-1]}')
        countDown += 1
        if n != -1:
            staircase(n + 1)
    else:
        print('Not Draw!')

staircase(int(input("Enter Input : ")))