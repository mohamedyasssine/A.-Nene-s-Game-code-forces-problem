t=int(input())
for i in range(t) :
    a,b = map(int, input().split(" "))
    l=list(map(int,input().split(" ")))
    l3=[]
    m = min(l) - 1

    print(*[min(m,i) for i in list(map(int,input().split()))])