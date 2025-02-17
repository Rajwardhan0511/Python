
def outer():    
    def inner():
        print("Hello")
    return inner

(outer())()

outer()()

inner = outer()
inner()
