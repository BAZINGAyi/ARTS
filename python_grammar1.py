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
    f = open('algorithm-1.py', encoding='utf-8')
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


# Question6: Generator function with external state
def generator_function_with_external_state():
    # If you want your generator to exposer the external state to the use,
    # don't forget that you can simply implement it as a class and then put
    # the generator function in the __iter() method. such as:
    from collections import deque
    class linehistory:
        def __init__(self, lines, histlen=3):
            self.lines = lines
            self.history = deque(maxlen=histlen)

        def __iter__(self):
            for lineno, line in enumerate(self.lines, 1):
                self.history.append((lineno, line))
                yield line

        def clear(self):
            self.history.clear()

    with open('algorithm-1.py', encoding='utf-8') as f:
        lines = linehistory(f)
        for line in lines:
            if 'print' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')

    # About the generator, it is easy to fall into trap of the function
    # omnipotent. If the generator function needs to deal with other parts of
    # your program(such as exposing property values, allowing control via method
    # calls, etc). it can make your code exceptions more complicated. If this
    # is the case, consider using the way defined classes described above.

    # If you want not to use the for in the traverse operation. you can use
    # iter() function.
    f = open('algorithm-1.py', encoding='utf-8')
    lines = linehistory(f)
    it = iter(lines)
    print(next(it))
    print(next(it))


# Question7: Iterator slice
def iterator_slice():
    # you want to get a object that generated by an iterator, but the standard
    # slice operation does not.
    # use the itertools.islice()
    def count(n):
        while True:
            yield n
            n += 1

    c = count(0)
    # c[10:20] will have a error
    # Now using islice()
    import itertools
    for x in itertools.islice(c, 10, 20):
        print(x)

    # The Iterator and generator can not used the standard cut operation,
    # because the length of them that we don't know. The islice() can return a
    # iterator that generated by the elements, it can traverse and drop the
    # elements until the slice start index position.

    # But the islice() function will consume the data in the incoming iterator.


# Question8: jump the start of the iterator object
def jump_the_start_of_the_iterator_object():
    # init file
    with open('.gitignore') as f:
        for line in f:
            print(line, end='')
    print("I'm as split---------------------")

    # If you want to skip the comment line at the beginning, you can do this:
    from itertools import dropwhile
    with open('.gitignore') as f:
        for line in dropwhile(lambda line: line.startswith('#'), f):
            print(line, end='')

    # if we know the number of line, we can use itertools.islice() instead of it
    from itertools import islice
    items = ['a', 'b', 'c', 1, 4, 10, 15]
    for x in islice(items, 3, None):
        print(x)
    # get the three numbers of start
    for x in islice(items, None, 3):
        print(x)


# Question9: Iterative combination of iterations
def iterative_combination_of_iterations():
    # Method1: itertools.permutations, Generate a tuple by scrambling the order
    # of the elements in the collection
    items = ['a', 'b', 'c']
    from itertools import permutations
    for p in permutations(items):
        print(p)

    # Method2: If you want to get all the permutations of the specified length,
    # you can pass an optional length parameter.
    for p in permutations(items, 2):
        print(p)

    # Method3: Use the itertools.combinations
    # Get all the combinations of elements in the input collection. but the
    # order of the elements is no longer important
    from itertools import combinations
    for c in combinations(items, 3):
        print(c)

    for c in combinations(items, 2):
        print(c)

    for c in combinations(items, 1):
        print(c)

    # Method4: When calculating the combination, once the element is selected,
    # it is removed from the candidate (for example, if the element 'a' has
    # already been selected, then it will not be considered again). The function
    # itertools.combinations_with_replacement() allows the same element to be
    # selected multiple times, such as:
    from itertools import combinations_with_replacement
    for c in combinations_with_replacement(items, 3):
        print(c)


# Question10: Iterative index value iteration
def iterative_index_value_iteration():
    # You want to track the index of th element being processed while iterating
    # over a sequence
    # Use the enumerate() of the enumerate()
    my_list = ['a', 'b', 'c']
    for idx, val in enumerate(my_list):
        print(idx, val)

    # you change the start value
    my_list = ['a', 'b', 'c']
    for idx, val in enumerate(my_list, 1):
        print(idx, val)

    # you can use it in traversing files
    def parse_data(filename):
        with open(filename, 'rt') as f:
            for lineno, line in enumerate(f, 1):
                fields = line.split()
                try:
                    count = int(fields[1])
                except ValueError as e:
                    print('Line {}: Parse error: {}'.format(lineno, e))
    parse_data('.gitignore')


# Question11： Iterating multiple sequences simultaneously
def iterating_multiple_sequences_simultaneously():
    # you want to iterating multiple sequences simultaneously
    # use the zip()
    xpts = [1, 5, 4, 2, 10, 7]
    ypts = [101, 78, 37, 15, 62, 99]
    for x, y in zip(xpts, ypts):
        print(x, y)
    # Once one of the sequences ends, the iteration ends.
    a = [1, 2, 3]
    b = ['w', 'x', 'y', 'z']
    for i in zip(a, b):
        print(i)

    # the zip_longest() will stop when the iterating arrive at the end of the
    # longest list
    from itertools import zip_longest
    for i in zip_longest(a, b, fillvalue=0):
        print(i)

    # Use the zip to generate a dict
    headers = ['name', 'shares', 'price']
    values = ['ACME', 100, 490.1]
    s = dict(zip(headers, values))
    print(s)

    for name, val in zip(headers, values):
        print(name, '=', val)

    # use the More than two sequences of parameters
    a = [1, 2, 3]
    b = [10, 11, 12]
    c = ['x', 'y', 'z']
    for i in zip(a, b, c):
        print(i)

    # The final point is that zip() will create an iterator to return as the
    # result. If you need to store the paired values ​​in a list, use the list()
    # function. such as:
    zip(a, b)
    print(list(zip(a, b)))


# Question12: Iteration of elements on different collections
def iteration_of_elements_on_different_collections():
    from itertools import chain
    a = [1, 2, 3, 4]
    b = ['x', 'y', 'z']
    for x in chain(a, b):
        print(x)


if __name__ == '__main__':
    # uses_asterisk()

    # delayed_binding()

    # manual_traversal_iterator()
    # proxy_iteration()
    # create_iterator_by_using_generator()
    # implement_an_iterator_protocol()
    # reverse_iteration()
    # generator_function_with_external_state()
    # iterator_slice()
    # jump_the_start_of_the_iterator_object()
    # iterative_combination_of_iterations()
    # iterative_index_value_iteration()
    # iterating_multiple_sequences_simultaneously()
    iteration_of_elements_on_different_collections()
