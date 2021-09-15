def print1toN(n):
    if n > 0:
        print1toN(n - 1)
        if n != 1:
            print(f'{n} ', end='')
    elif n <= 0:
        print(f'1 ', end='')

def printNto1(n):
    if n > 0:
        print(f'{n} ', end='')
        if n != 1:
            printNto1(n - 1)
    elif n <= 0:
        print(f'1 ',end='')

n = int(input("Enter Input : "))

print1toN(n)
printNto1(n)
