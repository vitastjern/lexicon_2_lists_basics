# Write a program that receives two numbers (factor and count) and creates a list with length of the 
# given count and contains only elements that are multiples of the given factor

factor = int(input())
count = int(input())
lst = []

for i in range(1, count+1):
    lst.append(factor * i)

print(lst)
