def greeting(name):
    print("Hi my name is " + name + ".")
    greeting2(name)
    print("Getting ready to say bye.")
    bye()

def greeting2(name):
    print("Hope you are doing well today " + name + ".")

def bye():
    print("Okay Goodbye!")

greeting("Maleeha")


# Notes: 
# When you call the greet2 function the greet function is partially completed.
# When you call a function from another function, the calling function is pausedd in a partially complete state. 