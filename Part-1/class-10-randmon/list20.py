from random import choices
numbers=[101,201,301,401,501,601,11,7,8,18,31,1055,232,99,199,299,399,499,599,699]
print(len(numbers))

selected_numbers=choices(numbers,k=5)
print(selected_numbers)