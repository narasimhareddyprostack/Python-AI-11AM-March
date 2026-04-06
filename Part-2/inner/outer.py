def outer():
    print("outer fn started")


    def inner():
        print("Inside inner function")
    inner()
    inner()
    inner()

outer()