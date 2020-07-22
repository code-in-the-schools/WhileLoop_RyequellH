import random
e = random.randint(-100,100)
found = False
while found == False: 
 d = int(input("Guess any number"))
 if d==e:
   found = True
   print("You've Just won!!!")
          elif d>e:
  print(str(d), "is more then it")
elif d<e:
  print(str(e, "is less then it"))
else:
  print("This isnt a number, try again.")

  