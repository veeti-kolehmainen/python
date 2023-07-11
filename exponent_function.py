# print(2**3)

def raise_to_power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
        # print(result)
    return result

print(raise_to_power(3, 3))