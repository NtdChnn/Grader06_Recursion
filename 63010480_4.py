ans = 9999
def counter(ip, d, k):
    global ans
    if len(d) == k:
        ll = [ip[i] for i in range(len(ip)) if d[i]]
        a = 1
        e = 0
        if len(ll) != 0:
            for i in ll:
                s, b = i.split(' ')
                a *= int(s)
                e += int(b)
            if abs(a-e) < ans:
                ans = abs(a-e)
    else:
        d[k] = 0
        counter(ip, d, k + 1)
        d[k] = 1
        counter(ip, d, k + 1)

ip = input("Enter Input : ").split(',')
d = [0]*len(ip)
counter(ip, d, 0)
print(ans)