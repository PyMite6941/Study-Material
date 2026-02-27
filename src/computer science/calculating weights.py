def dot(a,b):
    return sum(a * b for a,b in zip(a,b))

def neurons(a,b):
    return dot(a,b)

a = {1,2,3,4,5}
b = {5,4,3,2,1}
print(neurons(a,b))