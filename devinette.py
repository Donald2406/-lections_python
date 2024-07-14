import random
z=random.randint(1,100)
print("choisir un nombre entre 1 à 100")
i=6
while i>=0:
      print("essai n",i)
      n=int(input(""))
      print("proposition",n)
      if n<z:
         print("trop petit")
      elif n>z:
          print("trop grand")
      else:
          print("Bravo!! vous avez gagné")
          break
      i=i-1
if n!=z:
      print("desolé vous avez perdu")

