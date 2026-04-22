name =str(input("enter your name"))
subject = str(input("enter your subject"))
mark = int(input("enter your mark"))
if mark >= 100:
   print("invalid mark")
elif mark >= 85:
     print(f"welldone {name} you have got an A in {subject}, your mark is {mark}")
elif mark >= 70:
     print(f"welldone {name} you have got a B in {subject}, your mark is {mark}")
elif mark >= 64:
     print(f"welltried {name} you have got a C in {subject}, your mark is {mark}")
elif mark >= 49:
     print(f"keep trying {name} you have got a D in {subject}, your mark is {mark} ")
elif mark >= 40:
     print(f"sorry {name} you have got U in {subject}, your mark is {mark}")
