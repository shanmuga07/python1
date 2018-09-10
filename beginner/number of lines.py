fnam = input("Enter file name: ")
num_lines = 0
with open(fnam, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)
