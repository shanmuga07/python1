a=[]
c=int(input("Enter number of elements:"))
for i in range(1,c+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Largest element is:",a[c-1])
