# superior element is the number whose rightmost element is greater then them and rightmost number is already superior number

test_list = [8, 10, 6, 2, 9, 7]
c = 0
li = []

for i in range(len(test_list)):
    flag = True
    for j in range(i + 1, len(test_list)):
        if test_list[i] > test_list[j]:
            flag = False
            break
    if flag is True:
        c = c+1





print(c)
