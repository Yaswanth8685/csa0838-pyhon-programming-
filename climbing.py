n=int(input("N= "))
if (n==0):
   print(0)
if (n==1):
   print(1)
r=0
t=0
o=0
for i in range (1,n+1):
   r=o+t
   t=o
   o=r
print(r)
