# Queston1: 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？
# Answer: 这种解压方式适用于 元组，序列，字符串，文件对象，迭代器和生成器等确定长度的迭代对象


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


if __name__ == '__main__':
    # assign_variable()

    # assign_variable1()

    # record_n_elements_of_files()

    find_the_largest_or_smallest_n_elements()

