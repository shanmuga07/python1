To take input from the user
# lower = int(input("Enter lower range: "))
# upper = int(input("Enter upper range: "))

for n in range(lower, upper + 1):

   # order of number
   order = len(str(n))
    
   # initialize sum
   sum = 0

   # find the sum of the cube of each digit
   temp = n
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(n)
