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


def delete_list():
    # Method1: traverse in new list and delete in old list
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    print(id(a))
    # a[:] is new list
    print(id(a[:]))
    for i in a[:]:
        if i > 5:
            pass
        else:
            a.remove(i)
        print(a)
    print(id(a))

    # Method2: filter
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    b = filter(lambda x: x > 5, a)
    print(list(b))

    # Method3: list comprehensive
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    b = [i for i in a if i > 5]
    print(b)

    # Method4：Reverse order deletion Because the list is always 'moved forward',
    # it can be traversed in reverse order, even if the following elements are
    # modified, the elements that have not been traversed and their
    # coordinates remain unchanged.
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    print(id(a))
    for i in range(len(a) - 1, -1, -1):
        print(i)
        if a[i] > 5:
            pass
        else:
            a.remove(a[i])
    print(id(a))
    print(a)


def list_comprehension():
    # 求出列表所有奇数并构造新列表
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = [i for i in a if i % 2 == 1]
    print(res)

    # 用一行python代码写出1+2+3+10248
    from functools import reduce
    # 1.使用sum内置求和函数
    num = sum([1, 2, 3, 10248])
    print(num)
    # 2.reduce 函数
    num1 = reduce(lambda x, y: x + y, [1, 2, 3, 10248])
    print(num1)


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


def get_missing_letter():
    def get_missing_letter(a):
        s1 = set("abcdefghijklmnopqrstuvwxyz")
        s2 = set(a.lower())
        ret = "".join(sorted(s1 - s2))
        return ret
    print(get_missing_letter("python"))

    # generate a-z
    import string
    letters = string.ascii_lowercase
    print(letters)
    # 方法二:
    letters = "".join(map(chr, range(ord('a'), ord('z') + 1)))
    print(letters)


if __name__ == '__main__':
    # sorted_dict()
    # handle_dict()

    # handle_string()

    # handle_list()
    # delete_list()

    # list_math_calculate()

    get_missing_letter()
