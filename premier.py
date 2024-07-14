from math import*
a=int(input("entrer un nombre"))
i=2
while i< sqrt(a) and a%i!=0:
    i=i+1
if i>sqrt(a):
   print("premier")
else:
       print("pas premier")
