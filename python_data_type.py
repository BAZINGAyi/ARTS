# Question1: 对字典进行排序
def sorted_dict():
    d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
    d1 = sorted(d.items(), key=lambda x: x[1])
    print(d1)

    alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30},
             {'name': 'c', 'age': 25}]

    def sort_by_age(list1):
        return sorted(alist, key=lambda x: x['age'], reverse=True)

    print(sort_by_age(alist))


# Question2: 字典推导式
def handle_dict():
    iterable = {"a": 1, "b": 2, "c": 3, "d": 4}
    d = {value: key for (key, value) in iterable.items()}
    print(d)

    # 将 str1 变成字典
    str1 = "k:1|k1:2|k2:3|k3:4"

    def str2dict(str1):
        dict1 = {}
        for iterms in str1.split('|'):
            key, value = iterms.split(':')
            dict1[key] = value
        return dict1

    # 字典推导式
    d = {k: int(v) for t in str1.split("|") for k, v in (t.split(":"),)}
    print(d)


# Question3: 字符串操作
def handle_string():
    # 反转字符串
    print("astr"[::-1])


# Question4: 列表操作
def handle_list():
    # 获取超出长度的列表的切片，不会报错，会返回 []
    list_cut = ['a', 'b', 'c', 'd', 'e']
    print(list_cut[10:])

    # 列表推导式，生成公差为 11 的等差数列
    print([x * 11 for x in range(10)])

    # remove repeated elements
    # method1
    l1 = ['b', 'c', 'd', 'c', 'a', 'a']
    l2 = list(set(l1))
    print(l2)


# Question5: 集合的计算
def list_math_calculate():
    # 两个 list
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    set1 = set(list1)
    set2 = set(list2)
    print(set1 & set2)
    print(set1 ^ set2)
    print(set1 | set2)


if __name__ == '__main__':
    # sorted_dict()
    handle_dict()
    handle_string()
    handle_list()
    list_math_calculate()