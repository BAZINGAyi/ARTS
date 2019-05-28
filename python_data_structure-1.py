# Queston1: 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？
# Answer: 这种解压方式适用于 元组，序列，字符串，文件对象，迭代器和生成器等确定长度的迭代对象
from collections import OrderedDict


def assign_variable():
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    _, shares, price, _ = data
    print(shares)


# Question2: 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。
# 那么怎样才能从这个可迭代对象中解压出 N 个元素出来？
# Answer: 使用星号表达式，得到可迭代的对象。适用于不确定长度的迭代对象


def assign_variable1():
    # 计算去除首尾的平均值
    grades = [67, 89, 90, 100, 67, 55]
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

    # 星号表达式忽略
    record = ('ACME', 50, 123.45, (12, 18, 2012))
    name, *_, (*_, year) = record
    print(name, year)

    # 星号表达式传参
    records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4),
    ]

    def do_foo(x, y):
        print('foo', x, y)

    def do_bar(s):
        print('bar', s)

    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)

# Question3: 保留最后 N 个元素
# Answer: 使用 deque 数据结构


def search(lines, pattern, history=5):
    from collections import deque
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


def record_n_elements_of_files():
    """
    查找到目标支付串后，保留之前的 N 行
    """
    with open(r'leetcode-7.py') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)


# Question4: 查找最大或者最小的 N 个元素
# Answer:  使用堆队列 heapq 实现，原因是由于堆数据结构的特征，堆顶总是最大（或者最小）
# 的元素，同时堆顶也就表示着优先级最高的元素。进而每次取堆顶的值，就是我们题目中所要求的。


def find_the_largest_or_smallest_n_elements():
    import heapq
    # simple list
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    # complicated data structure
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    print(cheap)
    print(expensive)

    # In each operation, get the result with the highest priority value
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heap = list(nums)
    heapq.heapify(heap)
    # get the -4, default is min-heap
    print(heapq.heappop(heap))
    print(heap)
    # get the 1
    print(heapq.heappop(heap))
    print(heap)

# Question5: 实现一个优先队列，每次取出的操作总是优先级最高的那个
# Answer: 使用 heapq 堆的结构


def test_priority_queue():
    import heapq

    class PriorityQueue:
        def __init__(self):
            self._queue = []
            self._index = 0

        def push(self, item, priority):
            # -priority represents sequence from high to slow, likes 5 to 1.
            # because the heappop() always return the smallest elements

            # and the index can ensures that objects of the same priority
            #  are returned in order
            heapq.heappush(self._queue, (-priority, self._index, item))
            self._index += 1

        def pop(self):
            return heapq.heappop(self._queue)[-1]

    class Item:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return 'Item({!r})'.format(self.name)

    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())


# Question6: 怎样实现一个键对应多个值的字典（也叫 multidict）？
# Answer: 将多个值放入 list 或者 集合中, 或者使用 defaultdict 的数据结构

def multidict_dict():
    from collections import defaultdict

    multidict_list = {
        'a': [1, 2, 3],
        'b': [4, 5]
    }

    multidict_set = {
        'a': {1, 2, 3},
        'b': {4, 5}
    }

    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)

    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['b'].add(4)

    # defaultdict 会自动为将要访问的键（就算目前字典中并不存在这样的键）创建映射实体。
    #  如果你并不需要这样的特性，在一个普通的字典上使用 setdefault() 方法来代替。

    d = {}
    d.setdefault('a', []).append(1)
    d.setdefault('a', []).append(2)
    d.setdefault('b', []).append(4)


# Question7:  你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。
# Answer: 可以用 collections 中的 OrderedDict 类


def deal_ordered_dic():
    # 注意一个 OrderedDict 的大小是普通字典的两倍，因为内部维护着一个链表，在读取大量的
    # 数据时，需要权衡一下内存的印象。
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4

    for key in d:
        print(key, d[key])

    import json
    print(json.dumps(d))


# Question8: 怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）?
# Answer: 使用 zip(), sorted()
# Notice：zip() 将字典中的 key 和 value 反转，返回的迭代器只能访问一次
# 在普通字典上，执行数学运算，计算的值是键，不是值。进而一般需要 zip() 进行反转。

def calculate_dic():
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    # 正常思路中，当我们需要查找当前的最大价格和最小价格时，一般还需要 key 的信息
    # 仅能获取 value
    min(prices.values())  # Returns 10.75
    # 仅能获取 key
    min(prices, key=lambda k: prices[k])  # Returns 'FB'
    # 同时获取 key 和 value
    min_value = prices[min(prices, key=lambda k: prices[k])]  # (10.75, 'FB')

    # 使用 zip() 解决

    min_price = min(zip(prices.values(), prices.keys()))
    # min_price is (10.75, 'FB')

    max_price = max(zip(prices.values(), prices.keys()))
    # max_price is (612.78, 'AAPL')

    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    # prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
    #                   (45.23, 'ACME'), (205.55, 'IBM'),
    #                   (612.78, 'AAPL')]


# Question9: 怎样在两个字典中寻寻找相同点（比如相同的键、相同的值等等）？
# Answer: 利用字典本身提供的 keys() 和 items() 进行操作
# Notice：
# 1. keys（） 返回字典的 key 键集合的键视图对象，而键视图的一个很少
# 被了解的特性就是它们也支持集合操作，比如集合并、交、差运算，而不用转换成 set.
# 2. items() 也是一个 (键，值) 对的元素视图对象，支持集合操作。
# 3. values() 却不支持，从某种程度上说，以原因是值视图无法保证所有的值互不相同，
# 在执行某些操作时，会出现问题。

def find_common_in_dics():
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }

    # Find keys in common
    a.keys() & b.keys()  # { 'x', 'y' }
    # Find keys in a that are not in b
    a.keys() - b.keys()  # { 'z' }
    # Find (key,value) pairs in common
    a.items() & b.items()  # { ('y', 2) }

    # Make a new dictionary with certain keys removed
    c = {key: a[key] for key in a.keys() - {'z', 'w'}}
    # c is {'x': 1, 'y': 2}



if __name__ == '__main__':
    # assign_variable()

    # assign_variable1()

    # record_n_elements_of_files()

    # find_the_largest_or_smallest_n_elements()

    # test_priority_queue()

    # multidict_dict()

    # deal_ordered_dic()

    calculate_dic()


