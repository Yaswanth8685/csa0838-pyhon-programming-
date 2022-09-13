a=str(input("enter the month:"))
b=int(input("enter the date:"))
if a ==('january','febuary','march'):
   print("the season is winter")
elif a ==('april','may','june'):
   print("the season is summer")
elif a ==('july','august','september'):
   print("the season is spring")
else:
   print("the season is fall")

if(a=='march')and(b>20):
   print("the season is summer")
elif(a=='june')and(b>21):
   print("the season is spring")
elif(a=='september')and(b>22):
   print("the season is fall")
elif(a=='december')and(b>21):
   print("the season is winter")
