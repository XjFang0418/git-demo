# 遍历1-1000的水仙数，水仙数是指一个n位数，它的每个位上的数字的n次幂之和等于它本身。

# 定义一个函数，用于计算一个数字的每位数字的n次幂之和
def is_narcissistic(num):
    # 将数字转换为字符串，以便遍历每一位
    str_num = str(num)
    # 获取数字的位数
    n = len(str_num)
    # 计算每位数字的n次幂之和
    sum_of_powers = sum(int(digit) ** n for digit in str_num)
    # 如果计算结果等于原始数字，则返回True，否则返回False
    return sum_of_powers == num

# 遍历1-1000的每个数字
for i in range(1, 1001):
    # 如果数字是水仙数，则打印出来
    if is_narcissistic(i):
        print(i)
def is_narcissistic(num):
    # 将数字转换为字符串，以便遍历每一位
    str_num = str(num)
    # 获取数字的位数
    n = len(str_num)
    # 计算每位数字的n次幂之和
    sum_of_powers = sum(int(digit) ** n for digit in str_num)
    # 如果计算结果等于原始数字，则返回True，否则返回False
    return sum_of_powers == num
######
###？》》》》》》》》
