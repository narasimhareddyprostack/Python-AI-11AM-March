def outer():
    print("outer fn started")


    def inner():
        print("Inside inner function")
    
outer()
inner()
inner()
inner()
