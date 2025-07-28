def count_no_of_occur(li):
    l_s = [str(i) for i in li]
    list_to_str = ''.join(l_s)
    print('list_to_str', list_to_str)
    dic = {}
    for i in set(l_s):
        dic[i] = list_to_str.count(i)
    print(dic)


def coun_of_character(s):
    dic = {}
    for i in set(s):
        dic[i] = s.count(i)
    print(dic)


# Python – Extract elements with Frequency greater than K
def element_with_high_freq(li):
    l_s = [str(i) for i in li]
    list_to_str = ''.join(l_s)
    print('list_to_str', list_to_str)
    dic = {}
    for i in set(l_s):
        dic[i] = list_to_str.count(i)
    print(dic)
    k = 1
    ele = {key: val for key, val in dic.items() if val > k}
    print(list(ele.keys()))


def find_duplicate_item(li):
    duplicate = []
    for i in li:
        c = 0
        for j in range(len(li)):
            if i == li[j]:
                c = c + 1
                li[j] = '0'
        if c > 1 and i != '0':
            duplicate.append(i)
    print(duplicate)


def total_uniq_item_list(li):
    unique = []
    for i in li:
        c = 0
        for j in range(len(li)):
            if i == li[j]:
                c = c + 1
                li[j] = '0'
        if i != '0':
            unique.append(i)
    print(unique)


def total_uniq_item_list1(li):
    uniq = []
    for i in li:
        if i not in uniq:
            uniq.append(i)
    print(uniq)


def consecutive_num(li):
    pass


'''
Given an array arr[] of N positive integers. The task is to find the maximum for every adjacent pair in the array.
Input: 1 2 2 3 4 5
Output: 2 2 3 4 5
Read the input array i.e,arr1.
for i=1 to sizeofarray-1
find the max value between arr1[i] and arr1[i-1].
store the above value in another array i.e, arr2.
print the values of arr2.
'''


def max_adjacent(li):
    adj_arr = []
    for i in range(1, len(li)):
        adj_arr.append(max(li[i - 1], li[i]))
    print(adj_arr)


"""
Our task is to print the element which occurs 3 consecutive times in a Python list. 
Example :

Input : [4, 5, 5, 5, 3, 8]

Output : 5

Input : [1, 1, 1, 64, 23, 64, 22, 22, 22]

Output : 1, 22
"""


def is_occurrence_three_consecutively(li):
    li_con = []
    for i in range(len(li) - 2):
        if li[i] == li[i + 1] and li[i + 1] == li[i + 2]:
            li_con.append(li[i])
    print(li_con)


# like 1,2,3
def is_occurrence_three_consecutively_like_123(li):
    li_con = []
    for i in range(len(li) - 2):
        if li[i] + 1 == li[i + 1] and li[i + 1] + 1 == li[i + 2]:
            li_con.append((li[i], li[1 + 1], li[i + 2]))
    print(li_con)


"""
 Python Program to print all Possible Combinations from the three Digits
Last Updated : 29 Aug, 2020
Given 3 digits a, b, and c. The task is to find all the possible combinations from these digits.

Examples:

Input: [1, 2, 3]
Output:
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""


def combination_three_number(li):
    for i in range(len(li)):
        for j in range(len(li)):
            for k in range(len(li)):
                if li[i] != li[j] and li[j] != li[k] and li[i] != li[k]:
                    print(li[i], li[j], li[k])


def combination_pre_fun():
    # Python program to print all
    # the possible combinations

    from itertools import permutations

    # Get all combination of [1, 2, 3]
    # of length 3
    comb = permutations([1, 2, 3], 3)

    for i in comb:
        print(i)


"""
Given a list with some elements being a list of optional elements. The task is to find all the possible combinations 
from all options.
Input: test_list = [1,2,3]
Output: 
 [1], [1, 2], [1, 2, 3], [1, 3]
 [2], [2, 3], [3]
"""


def possible_combination(li=[1, 2, 3]):
    print(li)


"""
Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”] 
Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}] 
Explanation : Values mapped by custom key, “name” -> “Gfg”, “id” -> 3. 

Input : test_list = [“Gfg”, 10], test_list = [“name”, “id”] 
Output : [{‘name’: ‘Gfg’, ‘id’: 10}] 
Explanation : Conversion of lists to list of records by keys mapping.
"""


# (['govinda', 26, 'Shah', 3], ['name', 'id'])
def key_val_pair(test_list, key_list):
    li_pair = []
    for i in range(0, len(test_list), 2):
        print(i)
        li_pair.append({key_list[0]: test_list[i], key_list[1]: test_list[i + 1]})
    print(li_pair)


"""
Sometimes, while working with Python tuples list, we can have a problem in which we need to perform retention of
all the records where occurrences of K is N times. 
This kind of problem can come in domains such as web development and day-day programming.
Let’s discuss certain ways in which this task can be performed.

Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 2 
Output : [(4, 5, 5, 4)]
Input : test_list = [(4, 5, 5, 4), (5, 4,5 3)], K = 5, N = 3 
Output : [] 

"""


def retention_list_matching():
    test_list = [(4, 5, 5, 4), (5, 4, 5, 3)]
    k = 5
    n = 2
    req_list = [item for item in test_list if item.count(k)>= 2]
    print(req_list)




"""
The original list is : [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
The mapped Dictionary : {('a', 'b'): (1, 2), ('c', 'd'): (3, 4), ('e', 'f'): (5, 6)}
"""


def map_to_dic(test_list):
    dic = {}
    for i in test_list:
        dic[tuple(i[0:2])] = i[2:]
    print(dic)

"""
The original list is : [4, 5, 6, 3, 9]
The list after element duplication [4, 4, 5, 5, 6, 6, 3, 3, 9, 9]
"""
def make_duplicate_item(test_list = None,k =None):
    test_list = [4, 5, 6, 3, 9]
    k = 2
    dup_mix =[item for item in test_list for i in range(k)]
    print("duplicate_mix", dup_mix)

"""
The original list : [4, 5, 6]
The list after alternate repeating elements : [4, 4, 4, 6, 6, 6]
"""

def make_duplicate_alternate_item():
    test_list = [4, 5, 6]
    k = 3
    dup_alt_list = [item for idx, item in enumerate(test_list) if idx %2 == 0 for i in range(k) ]
    print('list_comp-dupli',dup_alt_list)


"""
nput : test_list = [4, 6, 7, 3, 1, 9, 2, 19], idx_list = [3, 1, 6] 
Output : [4, 6, 6, 7, 3, 3, 1, 9, 2, 2, 19] 
Explanation : All required index elements repeated, Eg. 6 repeated as it is at index 1.

Input : test_list = [4, 6, 7, 3, 1, 9, 2, 19], idx_list = [1, 6] 
Output : [4, 6, 6, 7, 3, 1, 9, 2, 2, 19] 
Explanation : All required index elements repeated, 6 repeated as it is at index 1. 
"""
def repeate_element_at_index():
    test_list = [4, 6, 7, 3, 1, 9, 2, 19]
    idx_list = [3, 1, 6]
    k = 2
    # rep_list = [item for idx, item in enumerate(test_list) if idx in idx_list for i in range(2)]
    rep_list = []
    for idx, item in enumerate(test_list):
        if idx in idx_list:
            rep_list.extend([item]*k)
        else:
            rep_list.append(item)

    print(rep_list)

"""
The original list is : [4, 5, 6]
List after extension and multiplication : [4, 5, 6, 12, 15, 18, 36, 45, 54, 108, 135, 162]
"""

def multiply_by_length_of_list_for_len_times():
    test_list =  [4, 5, 6]
    req_list=[]
    req_list.extend([4, 5, 6])
    for i in range(len(test_list)):
        req_list.extend([x*len(test_list) for x in test_list])

    print(req_list)

"""
Original Array : [‘Akash’ ‘Rohit’ ‘Ayush’ ‘Dhruv’ ‘Radhika’] 
New array : [‘AkashAkashAkash’ ‘RohitRohitRohit’ ‘AyushAyushAyush’ ‘DhruvDhruvDhruv’ ‘RadhikaRadhikaRadhika’]
"""

def multply_string():
    test_list= ['Akash', 'Riyansh','Manish']
    new_list = [item*3 for item in test_list]
    print(new_list)


"""
Input : test_list = [2, 3, 5, 6]
Output : { 2: 5, 3: 6}
"""

def list_key_val():
    test_list = [2, 3, 5, 6, 7, 8,9]
    dic = {}
    for i in range(len(test_list)-2):
        dic[test_list[i]]=test_list[i+2]
    print(dic)




if __name__ == '__main__':
    # count_no_of_occur([1, 2, 3, 1, 3])
    # coun_of_character("Govinda kumar")
    # find_duplicate_item([1, 2, 3, 1, 2, 1, 2, 4, 5])
    # total_uniq_item_list([1, 2, 2, 5, 8, 4, 4, 8])
    # total_uniq_item_list1([1, 2, 2, 5, 8, 4, 4, 8])
    # element_with_high_freq([1, 2, 2, 5, 8, 4, 4, 8])
    # max_adjacent([1, 2, 2, 3, 4, 5])
    # is_occurrence_three_consecutively([1, 1, 1, 64, 23, 64, 22, 22, 22])
    # is_occurrence_three_consecutively_like_123([1, 2, 3, 5, 4, 6, 7])
    # key_val_pair(['govinda', 26, 'Shah', 3], ['name', 'id'])
    # map_to_dic([['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]])
    # combination_three_number([1, 2, 3])
    # possible_combination()
    # retention_list_matching()
    # make_duplicate_item()
    # make_duplicate_alternate_item()
    # repeate_element_at_index()
    # multiply_by_length_of_list_for_len_times()
    # multply_string()
    list_key_val()
