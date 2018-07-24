c=input("enter the value:")
a=len(c)
while True:
    if " " in c:
        a=a-1
        if(" " not in c):
          break
        print(a)
        break
    else:
        print(a)
        break 
