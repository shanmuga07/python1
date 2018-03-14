lower=int(input("enter the lower range:"))
upper=int(input("Enter the upper range:"))
for j in range(lower,upper+1):
    if(j%7==0 and j%5==0):
      print(j)
