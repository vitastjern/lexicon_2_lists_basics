# Write a program that receives a single string containing numbers separated by a single space. 
# Print a list containing the opposite [comment: appears to mean negation] of each number.

numbers_txt = []  
numbers = []

def negate_lst(lst):
    return [-i for i in lst]


numbers_txt = input().split()

for number in range(len(numbers_txt)):
    current_nr = int(numbers_txt[number])
    numbers.append(current_nr)

print(negate_lst(numbers))
