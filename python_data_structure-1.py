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

# Question: 保留最后 N 个元素
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


if __name__ == '__main__':
    # assign_variable()

    # assign_variable1()

    record_n_elements_of_files()

