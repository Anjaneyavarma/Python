import math
inp = int(input())
if (inp%2 == 0):
    number = int(inp/2)
    x = number - 1
    k=3
    output = x
    print(output)
else:
    number = int((inp+1)/2)
    x = number - 1
    k=2
    output = 2*x
    print(output)
