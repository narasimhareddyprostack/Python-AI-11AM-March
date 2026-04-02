#create list of 10 randmon integers b/w 1 to 100
import random
numbers=range(1,100)
rand_numbers=random.choices(numbers,k=10)
print(rand_numbers)