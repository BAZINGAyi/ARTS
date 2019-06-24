

# Question1: * 的使用
def uses_asterisk():
    # 1. 可变长参数
    # *args 表示不定个数的且不带默认值的参数，后面不允许跟没有默认值的参数。并将接受到的参数
    # 解包成元组
    # **kwargs 表示不定个数且带默认值的参数，后面不允许跟有默认值的参数。并将接受到的参数
    # 解包成字典
    def f1(x, *args, y=0, **kwargs):
        print(args)
        print(kwargs)

    f1(1, 2, 3, y=4, z=5, w=12)
    # 可变长参数
    x, *y = (1, (1, 2), 2)
    print(y)

    # 2. 参数解包
    # * 将元组或者列表解包成不带默认值的参数
    # ** 将字典解包，将 value 赋值给带默认值的参数
    def f(x, y, z):
        print(x, y, z)
    f(*[1, 2], **{'z': 3})


# Question2: Python closures are associated with delayed binding
def delayed_binding():
    def multi():
        return [lambda x: i * x for i in range(4)]
    print([m(3) for m in multi()])


# Question3: Manual traversal iterator
def manual_traversal_iterator():
    # you want to traverse all the list of iterator, but want not to use the for
    def manual_iter():
        with open('algorithm-1.py', encoding='utf-8') as f:
            try:
                while True:
                    line = next(f)
                    print(line, end='')
            except StopIteration:
                pass
    manual_iter()
    # the next() is good method, and the StopIteration represents the end of
    # iteration.
    # Custom end return value

    with open('algorithm-1.py', encoding='utf-8') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')

    items = [1, 2, 3]
    # Get the iterator
    it = iter(items)  # Invokes items.__iter__()
    # Run the iterator
    print(next(it))  # Invokes it.__next__()
    print(next(it))  # Invokes it.__next__()
    print(next(it))  # Invokes it.__next__()
    try:
        next(it)
    except StopIteration:
        pass


# Question4: Proxy iteration
def proxy_iteration():
    # you build a Custom container object,it includes list, tuple, and other
    # iterator. you want to execute iteration operation on it.
    # Use the __iter__() method
    class Node:
        def __init__(self, value):
            self._value = value
            self._children = []

        def __repr__(self):
            return 'Node{!r}'.format(self._value)

        def add_child(self, node):
            self._children.append(node)

        def __iter__(self):
            return iter(self._children)

    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # Outputs Node(1), Node(2)
    for ch in root:
        print(ch)

    # The use of the iter() function here simplifies the code. Iter(s) simply
    # returns the corresponding iterator object by calling the s.__iter()
    # method, just as len(s) calls s.__len__(). the same.


if __name__ == '__main__':
    # uses_asterisk()

    # delayed_binding()

    #manual_traversal_iterator()
    proxy_iteration()