import pdb

def add(a, b):
    pdb.set_trace()  # Pauses execution and opens the debugger
    print(a,b)
    return a + b

result = add(5, 3)
print(result)

'''
n (next): Execute the next line.
s (step): Step into a function call.
c (continue): Continue execution until the next breakpoint.
l (list): Show source code around the current line.
p <variable>: Print the value of a variable.
q (quit): Exit the debugger.
'''