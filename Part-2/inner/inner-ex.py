def outer():
    print("Outer fun started")

    def login():
        print("Login success")
    def inner():
        print("Inner function")
    #return 100.5
    #return "Rahul"
    return login  #retun function ref

result=outer()
print(type(result))
result()          #we are invoking inner function from outside