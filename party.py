E=[]
L=[]
T= int(input("range T : "))
for i in range(T):
   e=int(input("E : "))
   E.append(e)
for i in range(T):
   l=int(input("L: "))
   L.append(l)
sum=0
Max=0
for i in range(T):
   sum+=E[i]-L[i]
   Max=max(sum,Max)
print("output",Max)
