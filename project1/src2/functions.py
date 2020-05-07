def square(x):
    print("In square: name is: ", __name__)
    return x * x

for i in range(10):
    print("{} squared is {}".format(i, square(i)))
print("In main: name is: ", __name__)