# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

#Note-- same with while loop
for i in range(6):
    if i == 4:
        break
    print(i)
else:
    print("Hello")

# '''
# when break statement is executed, which exits the loop before the else block runs. Thus, "Hello" is not printed.
# '''
# # different output
for i in range(6):
    print(i)
else:
    print("Hello")
# hello will print
