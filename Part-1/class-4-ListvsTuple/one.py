#Mutabilty vs Immutablity - list,tuple,set,dict
#create
enames=['Rahul','Sonia','Priyanka']
unames=('Rahul','Sonia','Priyanka')
eids={101,102,103,104}
emp={
    'eid':101,
    'ename':"Rahul",
    'esal':45000
}

enames[0]="Rahul Gandhi"  #List is Mutable object
print(enames)
unames[0]="Rahul Gandhi"  #TUple is Immutable Object