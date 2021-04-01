# Write a program that receives a list of integer numbers and a number n. The number n represents 
# the amount of numbers to remove from the list. You should remove the smallest ones.

lst = [ int(x) for x in input().split()]  # pretty! I need to remember this...
n = int(input())

sorted_lst = lst.copy()
sorted_lst.sort()

for x in range(n):
    lst.remove(sorted_lst[x])

print(lst)
