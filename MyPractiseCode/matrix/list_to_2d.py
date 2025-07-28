"""

input [ 1, 2, 3, 4, 5,6,7]
Output: [[1,2,3] [4,5,6],[7]]

"""

test_list = [1, 2, 3, 4, 5, 6, 7]
k = 3
exp_list = []
for item in range(0, len(test_list), 3):
    exp_list.append(test_list[item:k])
    k = k+3
print(exp_list)





