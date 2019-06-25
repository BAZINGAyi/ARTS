

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
    # method, just as len(s) calls s.__len__() the same.


# Question5: 使用生成器创建新的迭代模式
def create_iterator_by_using_generator():
    def frange(start, stop, increment):
        x = start
        while x < stop:
            yield x
            x += increment

    for n in frange(0, 4, 0.5):
        print(n)

    print(list(frange(0, 1, 0.125)))

    # A function needs a yield statement to convert it to a generator.
    # Unlike ordinary functions, generators can only be used for iterative
    # operations. Here is experiment that shows you the underlying working
    # mechanism of such a function:

    def countdown(n):
        print('Starting to count from', n)
        while n > 0:
            yield n
            n -= 1
        print('Done!')

    # Create the generator, notice no output appears
    c = countdown(3)
    # Run to first yield and emit a value
    print(next(c))
    print(next(c))
    print(next(c))
    # Have a exception, but the 'for' statement can resolve it
    # print(next(c))


# Question4: Implement an iterator protocol
def implement_an_iterator_protocol():
    # So far, there is most easiest way to implement an iterator is By Using
    # the generator
    class Node:
        def __init__(self, value):
            self._value = value
            self._children = []

        def __repr__(self):
            return 'Node({!r})'.format(self._value)

        def add_child(self, node):
            self._children.append(node)

        def __iter__(self):
            return iter(self._children)

        def depth_first(self):
            yield self
            for c in self:
                yield from c.depth_first()

    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)
    # Outputs Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)

    # The iterator protocol of python requires __iter()__ return a special
    # iterator object. This iterator object implements the __next__() method and
    # identifies the completion of the iteration through the StopIteration
    # exception. However, implementing these is often cumbersome.
    class DepthFirstIterator(object):
        '''
        Depth-first traversal
        '''

        def __init__(self, start_node):
            self._node = start_node
            self._children_iter = None
            self._child_iter = None

        def __iter__(self):
            return self

        def __next__(self):
            # Return myself if just started; create an iterator for children
            if self._children_iter is None:
                self._children_iter = iter(self._node)
                return self._node
            # If processing a child, return its next item
            elif self._child_iter:
                try:
                    nextchild = next(self._child_iter)
                    return nextchild
                except StopIteration:
                    self._child_iter = None
                    return next(self)
            # Advance to the next child and start its iteration
            else:
                self._child_iter = next(self._children_iter).depth_first()
                return next(self)

    class Node2:
        def __init__(self, value):
            self._value = value
            self._children = []

        def __repr__(self):
            return 'Node({!r})'.format(self._value)

        def add_child(self, node):
            self._children.append(node)

        def __iter__(self):
            return iter(self._children)

        def depth_first(self):
            return DepthFirstIterator(self)

    root = Node2(0)
    child1 = Node2(1)
    child2 = Node2(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node2(3))
    child1.add_child(Node2(4))
    child2.add_child(Node2(5))

    for ch in root.depth_first():
        print(ch)


# Question5: Reverse iteration
def reverse_iteration():
    # use reversed
    a = [1, 2, 3, 4]
    for x in reversed(a):
        print(x)

    # Reverse iteration only take effect if the size of the object is
    # pre-determined or if the object implements __reversed__ method.
    # If neither of them matches, you must first convert the object to a list,
    # such as
    # Print a file backwards
    f = open('algorithm-1.py',  encoding='utf-8')
    for line in reversed(list(f)):
        print(line, end='')
    # but convert a iterator to a list needs larges of memory

    # we can do it by using __reversed()__ method on custom class
    class Countdown:
        def __init__(self, start):
            self.start = start

        # Forward iterator
        def __iter__(self):
            n = self.start
            while n > 0:
                yield n
                n -= 1

        # Reverse iterator
        def __reversed__(self):
            n = 1
            while n <= self.start:
                yield n
                n += 1

    for rr in reversed(Countdown(30)):
        print(rr)
    for rr in Countdown(30):
        print(rr)


if __name__ == '__main__':
    # uses_asterisk()

    # delayed_binding()

    # manual_traversal_iterator()
    # proxy_iteration()
    # create_iterator_by_using_generator()
    # implement_an_iterator_protocol()
    reverse_iteration()
