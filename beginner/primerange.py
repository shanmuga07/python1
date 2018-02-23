lower = int(input(" "))
upper = int(input(" "))

print("Prime numbers between",lower,"and",upper,"are:")

for a in range(lower,upper + 1):
   if num > 1:
       for i in range(2,a):
           if (a % i) == 0:
               break
       else:
           print(a)
