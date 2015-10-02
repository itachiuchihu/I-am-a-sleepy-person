N=int(input())
A=input().split()
for i in range (N):
    A[i]=int(A[i])
print(A)
i=0
while i<N:
    k=A[i]
    S1=0
    S2=0
    for L in range(N):
        if A[i]>A[L]:
            S1+=1
    if S1==(N-1)/2:
        print('Answer=',A[i])
    i+=1

