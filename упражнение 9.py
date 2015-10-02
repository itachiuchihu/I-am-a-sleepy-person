A = [0] * int(input())
for i in range(len(A)):
    A[i] = int(input())
if len(A)%2==0:
    k=-1
    l=0
    B=[]
    while l<(len(A)/2):
        B=B+[A[l]]+[A[k]]
        k=k-1
        l+=1
else:
    k=-1
    l=0
    B=[]
    while l<(len(A)-1)/2:
        B=B+[A[l]]+[A[k]]
        k=k-1
        l+=1
        if l==(len(A)-1)/2:
            B=B+[A[l]]
print(B)

