def say_hello():
    print("Hello!")

def repeat(function, n):
    for n in range(n):
        function()

repeat(say_hello, 3)