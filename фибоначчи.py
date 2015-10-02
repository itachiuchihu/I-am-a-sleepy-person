A=input().split()
for i in range (len(A)):
    A[i]=int(A[i])
k=A[0]
n=A[1]
B=[1]*k
if n<=(k-1):
    print('Answer=',B[n])
else:
    L=len(B)
    while L<=n:
        S=0
        for i in range(k):
            S=S+B[i]
        B=B+[S]
        C=B.pop(0)
        if L==n:
            answ=S
            print('Answer=',answ)
        L+=1





