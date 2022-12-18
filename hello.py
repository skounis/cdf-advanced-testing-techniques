def addthis(x,y):
    print(f"You provided x and y: {x} of type {type(x)}, {y} of type {type(y)}") 
    try:
        result = x+y
    except TypeError as exception:
        print(f"Wrong type provided: {exception}")
        result = int(x) + int(y)
    print(f"Which make: {result}")
    return result

print( addthis(1,2) )
print( addthis(1,"4") )
print( addthis(1,"two") )
