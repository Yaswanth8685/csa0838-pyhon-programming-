g=input("enter the grade (A/B :")
s=int(input("salary:$"))
if (g=='A' and s<=10000):
   print("total salary : $",((s//7)+s))
elif(g=='A' and s>10000):
   print("total salary :$",((s//5)+s))
elif(g=='B' and s<=10000):
   print("total salary :$",((s//12)+s))
elif(g =='B' and s>10000):
   print("total salary :$",((s//10)+s))
   print("wrong input")
