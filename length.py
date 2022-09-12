str=input("enter the string: ")
length=len(str)
str=str.lower()
mid=length//2
rev=-1
for x in range(mid):
   if str[x]==str[rev]:
      x+=1
      rev-=1
   else:
      print(str,"is not a palindrome")
      break
else:
      print("str is a palindrome")
