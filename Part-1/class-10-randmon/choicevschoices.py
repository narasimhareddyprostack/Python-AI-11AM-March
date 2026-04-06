import random
enames=['Rahul','Sonia','Priya','Veena','Harshitha','SR']
#select one ramdon element from sequence ie list
print(random.choice(enames))


#select list of 3 ramdon element from sequence ie list
print(random.choices(enames,k=3))
