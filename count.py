def countwords(s):
   if s.strip()== "" :
      return o
   words=s.split()
   return len(words)
if __name__=="__main__":
   s=input("enter the string")
   print("no of words:",countwords(s))