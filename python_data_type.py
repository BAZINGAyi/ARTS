# Question1: 字典


class StudyDict(object):
    def __init__(self):
        pass

    @staticmethod
    def understanding_dict():
        # 给定产品的 ID 返回价格
        def find_product_price(products, product_id):
            for id, price in products:
                if id == product_id:
                    return price
            return None

        products = [
            (143121312, 100),
            (432314553, 30),
            (32421912367, 150)
        ]
        # 如果有 n 个元素，时间复杂度 O(n).
        # 如果对列表排序，然后进行二分查找，也需要 O(logn).
        # 排序还需要 O(nlogn)

        print('The price of product 432314553 is {}'.format(
            find_product_price(products, 432314553)))

        # 使用字典，仅仅需要 O（1）
        products = {
            143121312: 100,
            432314553: 30,
            32421912367: 150
        }
        print(
            'The price of product 432314553 is {}'.format(products[432314553]))

        # 找出这些商品有多少不同的价格
        # 使用列表 O(n^2)
        # list version
        def find_unique_price_using_list(products):
            unique_price_list = []
            for _, price in products:  # A
                if price not in unique_price_list:  # B
                    unique_price_list.append(price)
            return len(unique_price_list)

        products = [
            (143121312, 100),
            (432314553, 30),
            (32421912367, 150),
            (937153201, 30)
        ]
        print('number of unique price is: {}'.format(
            find_unique_price_using_list(products)))

        # 使用集合, O(n)
        # set version
        def find_unique_price_using_set(products):
            unique_price_set = set()
            for _, price in products:
                unique_price_set.add(price)
            return len(unique_price_set)

        products = [
            (143121312, 100),
            (432314553, 30),
            (32421912367, 150),
            (937153201, 30)
        ]
        print('number of unique price is: {}'.format(
            find_unique_price_using_set(products)))

        # 假如有 100000 个商品
        import time
        id = [x for x in range(0, 100000)]
        price = [x for x in range(200000, 300000)]
        products = list(zip(id, price))

        # 计算列表版本的时间
        start_using_list = time.perf_counter()
        find_unique_price_using_list(products)
        end_using_list = time.perf_counter()
        print(
            "time elapse using list: {}".format(
                end_using_list - start_using_list))

        # 计算集合版本的时间
        start_using_set = time.perf_counter()
        find_unique_price_using_set(products)
        end_using_set = time.perf_counter()
        print(
            "time elapse using set: {}".format(end_using_set - start_using_set))

        # dict structure: Old python version
        info = {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'}
        # The structure of the storage is as follows
        # entries = [
        # ['--', '--', '--']
        # [-230273521, 'dob', '1999-01-01'],
        # ['--', '--', '--'],
        # ['--', '--', '--'],
        # [1231236123, 'name', 'mike'],
        # ['--', '--', '--'],
        # [9371539127, 'gender', 'male']
        # ]

        # new dict structure:
        # indices = [None, 1, None, None, 0, None, 2]
        # entries = [
        # [1231236123, 'name', 'mike'],
        # [-230273521, 'dob', '1999-01-01'],
        # [9371539127, 'gender', 'male']
        # ]


    @staticmethod
    def sorted_dict():
        d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
        d1 = sorted(d.items(), key=lambda x: x[1])
        print(d1)

        alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30},
                 {'name': 'c', 'age': 25}]

        def sort_by_age(list1):
            return sorted(alist, key=lambda x: x['age'], reverse=True)

        print(sort_by_age(alist))

    @staticmethod
    def handle_dict():
        # 字典推导式
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


# Question4: 列表
class StudyList(object):
    def __init__(self):
        pass

    @staticmethod
    def understanding_list():
        l = [1, 2, 3]
        l.__sizeof__()  # 64

        tup = (1, 2, 3)
        tup.__sizeof__()  # 48

        # 事实上，由于列表是动态的，所以它需要存储指针，来指向对应的的元素（上述例子中，对于 int 型
        # ，8 字节）。另外，由于列表可变，所以需要额外存储已经分配的长度
        # 大小（8 字节），这样才可以实实时追踪列表空间的使用情况，当空间不足时，及时分配额外空间。
        l = []
        l.__sizeof__()  # 空列表的存储空间为 40 字节
        l.append(1)
        l.__sizeof__()
        # 72  加入了元素 1 之后，列表为其分配了可以存储 4个元素的空间(72 - 40) / 8 = 4
        l.append(2)
        l.__sizeof__()  # 72 // 由于之前分配了空间，所以加入元素 2，列表空间不变
        l.append(3)
        l.__sizeof__()  # 72 // 同上
        l.append(4)
        l.__sizeof__()  # 72 // 同上
        l.append(5)
        l.__sizeof__()
        # 104 // 加入元素5 之后，列表的空间不足，所以又额外分配了可以存储 4 个元素的空间
        # Python 的每次分配空间都会额外分配一些，增加/删除的操作均为 O（1）

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

        # 过滤元素，元素是偶数，并且在 list 位置也是偶数
        def num_list(num):
            return [i for i in num if i % 2 == 0 and num.index(i) % 2 == 0]

        num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = num_list(num)
        print(result)

        # 让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',
        # 变成'1355798642'

        # 方法一
        def func1(l):
            if isinstance(l, str):
                l = [int(i) for i in l]
            l.sort(reverse=True)
            for i in range(len(l)):
                if l[i] % 2 > 0:
                    l.insert(0, l.pop(i))
            print(''.join(str(e) for e in l))

        # 方法二
        def func2(l):
            print("".join(
                sorted(l, key=lambda x: int(x) % 2 == 0 and 20 - int(x) or int(
                    x))))

        func1('1982376455')
        func2('1982376455')

    @staticmethod
    def merge_list():
        # To merge these two lists, you cannot use extend.
        def loop_merge_sort(l1, l2):
            tmp = []
            while len(l1) > 0 and len(l2) > 0:
                if l1[0] < l2[0]:
                    tmp.append(l1[0])
                    del l1[0]
                else:
                    tmp.append(l2[0])
                    del l2[0]
            while len(l1) > 0:
                tmp.append(l1[0])
                del l1[0]
            while len(l2) > 0:
                tmp.append(l2[0])
                del l2[0]
            return tmp

    @staticmethod
    def list_math_calculate():
        # Question5: 集合的计算
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
    studyDict = StudyDict()
    # studyDict.sorted_dict()
    # studyDict.handle_dict()
    studyDict.understanding_dict()

    # handle_string()

    # studyList = StudyList()
    # studyList.understanding_list()
    # studyList.handle_list()
    # studyList.delete_list()
    # studyList.list_math_calculate()
    # studyList.list_comprehension()

    # get_missing_letter()

    # test_dict = {'a':1, 'b':2}



