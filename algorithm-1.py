# Question1: 写一个函数找出一个整数数组中，第二大的数
def find_the_second_largest_number_in_ar_arrays_of_integers(num_list):
    # Method1: use sorted
    tmp_list = sorted(num_list)
    print("方法一\nSecond_large_num is :", tmp_list[-2])

    # Method2:
    one = num_list[0]
    two = num_list[0]
    for i in range(1, len(num_list)):
        if num_list[i] > one:
            two = one
            one = num_list[i]
        elif num_list[i] > two:
            two = num_list[i]
    print("方法二\nSecond_large_num is :", two)

    # 方法三
    # 用 reduce 与逻辑符号 (and, or)
    # 基本思路与方法二一样，但是不需要用 if 进行判断。
    from functools import reduce
    num = reduce(lambda ot, x: ot[1] < x and (ot[1], x) or ot[0] < x and (
    x, ot[1]) or ot, num_list, (0, 0))[0]

    def fin2(ot, x):
        b = ot[1] < x and (ot[1], x) or ot[0] < x and (x, ot[1]) or ot
        print(b)
        return b

    reduce(fin2, num_list, (0, 0))
    print("方法三\nSecond_large_num is :", num)


if __name__ == '__main__':
    find_the_second_largest_number_in_ar_arrays_of_integers(
        [3, 1, 4, 1, 3, 4, 6565, 12])
