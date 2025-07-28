# 5 -1
# 2-0
# 1

def number_to_binary():
    num = 17
    print(bin(num).replace('0b','')) #decimal to binary
    binary = []
    while num >= 1:
        binary.append(str(num % 2))
        num = num // 2
    binary_str = ''.join(binary[::-1])
    print(binary_str)


def binary_to_number():
    bin_val = '1011'
    print(int(bin_val, 2)) # binary to decimal
    num = 0
    for i in range(len(bin_val)):
        num += pow(int(bin_val[i]) * 2, len(bin_val) - 1 - i)
    if int(bin_val[len(bin_val) - 1]) == 0:
        num = num - 1
    print(num)


# Python code to convert from Binary
# to Hexadecimal using int() and hex()
def binToHexa(n):
    # convert binary to int
    num = int(n, 2)

    # convert int to hexadecimal
    hex_num = hex(num)
    oct_num = oct(num)
    return (hex_num, oct_num)

def enumerate_list():

    nested_list = [[1, 2, 3], [4, 5], [7, 8]]

    for i, inner_list in enumerate(nested_list):
        for j, element in enumerate(inner_list):
            print(f"Value at index ({i}, {j}): {element}")




if __name__ == '__main__':
    # number_to_binary()
    binary_to_number()
    print(binToHexa('111101111011'))
    print(hex(101))
