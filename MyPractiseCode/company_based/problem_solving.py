"""
Questions 1 Problem Statement – Bela teaches her daughter to find the factors of a given number.
When she provides a number to her daughter, she should tell the factors of that number.
Help her to do this, by writing a program. Write a class FindFactor.java and write the main method in it.
Note :

If the input provided is negative, ignore the sign and provide the output. If the input is zero
If the input is zero the output should be “No Factors”.
Sample Input 1:
54

Sample Output 1:
1, 2, 3, 6, 9, 18, 27, 54

Sample Input 2:
-1869

Sample Output 2 :
1, 3, 7, 21, 89, 267, 623, 1869

"""


def find_factor_of_num():
    num = -1869
    factors_number = [item for item in range(1, abs(num) + 1) if abs(num) % item == 0] if num != 0 else "Not Factor"
    print(factors_number)


"""
Question 3 Problem Statement – Mayuri buys “N” no of products from a shop. The shop offers a different percentage of discount on each item. She wants to know the item that has the minimum discount offer, so that she can avoid buying that and save money.
[Input Format: The first input refers to the no of items; the second input is the item name, price and discount percentage separated by comma(,)]
Assume the minimum discount offer is in the form of Integer.
Note: There can be more than one product with a minimum discount.

Sample Input 1:
4
mobile,10000,20
shoe,5000,10
watch,6000,15
laptop,35000,5
Sample Output 1:
shoe
Explanation: The discount on the mobile is 2000, the discount on the shoe is 500, 
the discount on the watch is 900 and the discount on the laptop is 1750. 
So the discount on the shoe is the minimum.

"""


def find_minimum_discount():
    items = [("mobile", 10000, 20),
             ("shoe", 5000, 10),
             ("watch", 6000, 15),
             ("laptop", 35000, 5)]

    items.sort(key=lambda x: (x[1] * x[2]) // 100)
    print(items[0][0])


"""
Question 5 Problem Statement –
Capgemini in its online written test has a coding question, wherein the students are given a string with multiple 
characters that are repeated consecutively. You’re supposed to reduce the size of this string using
mathematical logic given as in the example below :

Input :
aabbbbeeeeffggg

Output:
a2b4e4f2g3

Input :
abbccccc

Output:
ab2c5
"""


def count_consecutive_letter():
    letter = "kaabbbbeeeeffggg"
    list_str_count = ''.join([ch + str(letter.count(ch)) for ch in set(letter)]).replace('1', '')
    print(list_str_count)


"""
Input:
m = 6
n = 30

Output:
285

Integers divisible by 6 are 6, 12, 18, 24, and 30. Their sum is 90.
Integers that are not divisible by 6 are 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 25, 26, 27, 28, and 29. Their sum is 375.
The difference between them is 285 (375 – 90).
"""


def sum_difference_range_divide_or_not_divide_by_m():
    n, m = 30, 6
    diff = abs(sum([item for item in range(n) if item % 6 == 0]) - sum([item for item in range(n) if item % 6 != 0]))
    print(diff)


"""
Replacecharacter(Char str1, Char ch1, Int 1, Char ch2)

Assumption

This string has only alphabets that are in lower case.

Example

Input:
str: apples
ch1: a
ch2: p

Output:
paales

Explanation
All the ‘a’ in the string is replaced with ‘p’. And all the ‘p’s are replaced with ‘a’.
"""


def replace_character():
    str = "apples"
    ch1 = "a"
    ch2 = "p"
    new_str = ''
    for ch in str:
        if ch == ch1:
            ch = ch2
        elif ch == ch2:
            ch = ch1
        else:
            ch = ch
        new_str = new_str + ch
    print(new_str)


"""
18. Create web access management to the kth largest number. It will accept an integer k and an array arr as 
its conditions and has to return the greatest element based on the value of k. 
That is, if k = 0, return the greatest element. If k = 1, 
return the second greatest element, and so on.
Example

Suppose the array contains values like {74, 85, 102, 99, 101, 56, 84} and the integer k is 2. 
The method will return 99, the third greatest element, as there are only two (according to the value of k) 
values greater than 99 (101 and 102)
"""


def kth_largest_number():
    test_list = [74, 85, 102, 99, 101, 56, 84]
    k = 4  # if k = 0, return the greatest element. If k = 1,
    test_list.sort()
    print(test_list)
    print(test_list[len(test_list) - (k + 1)])


def kth_largest_item_no_pre_fun():
    test_list = [74, 85, 102, 99, 101, 56, 84]
    k = 4  # if k = 0, return the greatest element. If k = 1,
    max_num = test_list[0]
    max_2 = 0
    for item in test_list:
        if max_num < item:
            max_num = item

    for item in test_list:
        if max_2 < item != max_num:
            max_2 = item
    print(max_num, max_2)


def babble_sort():
    # test_list = [2, 1, 4, 6, 3]
    test_list = [123, 21, 34, 45, 25, 675, 23, 44, 55, 900]
    c = 0
    for i in range(len(test_list)):
        print(test_list[i])
        for j in range(i + 1, len(test_list)):
            if test_list[i] > test_list[j]:
                temp = test_list[i]
                test_list[i] = test_list[j]
                test_list[j] = temp
                c = c + 1

    print(test_list, c)


"""
1 1 2 2 3 3
Output:
1x – 1y = 0
"""


def find_straight_line():
    test_list = [1, 1, 2, 2, 3, 3]
    flag = True
    for i in range(1, len(test_list), 2):
        print(test_list[i], test_list[i - 1])
        if test_list[i] != test_list[i - 1]:
            flag = False
            break

    if flag is True:
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    # find_factor_of_num()
    # find_minimum_discount()
    # count_consecutive_letter()
    # sum_difference_range_divide_or_not_divide_by_m()
    # replace_character()
    # kth_largest_number()
    # kth_largest_item_no_pre_fun()
    # babble_sort()
    find_straight_line()
