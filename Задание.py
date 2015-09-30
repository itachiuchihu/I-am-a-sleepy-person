from random import*
L=[str(randint(0,100)) for i in range (1000000)]
f=open('int_data.txt','w')
f.write(str(L))
f.close()
f=open('int_data.txt','r')
P=[line.strip() for line in f]
f.close()
print(P)
