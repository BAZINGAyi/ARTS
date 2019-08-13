# 遍历一个object的所有属性，并print每一个属性名？
def traverse_all_property_in_class():
    class Car:
        def __init__(self, name, loss):  # loss [价格，油耗，公里数]
            self.name = name
            self.loss = loss

        def getName(self):
            return self.name

        def getPrice(self):
            # 获取汽车价格
            return self.loss[0]

        def getLoss(self):
            # 获取汽车损耗值
            return self.loss[1] * self.loss[2]

    Bmw = Car("BMW", [60, 9, 500])  # 实例化一个宝马车对象
    print(getattr(Bmw, "name"))  # 使用getattr()传入对象名字,属性值。
    print(dir(Bmw))  # 获Bmw所有的属性和方法\


# Question2: Write a class and let it support as many operators as possible?
def support_many_operators():
    class Array:
        __list = []

        def __init__(self):
            print("constructor")

        def __del__(self):
            print("destruct")

        def __str__(self):
            return "this self-defined array class"

        def __getitem__(self, key):
            return self.__list[key]

        def __len__(self):
            return len(self.__list)

        def Add(self, value):
            self.__list.append(value)

        def Remove(self, index):
            del self.__list[index]

        def DisplayItems(self):
            print("show all items---")
            for item in self.__list:
                print(item)


class StudyOOP():

    def understand_OOP(self):
        class Document():
            def __init__(self, title, author, context):
                print('init function called')
                self.title = title
                self.author = author
                self.__context = context  # __ 开头的属性是私有属性

            def get_context_length(self):
                return len(self.__context)

            def intercept_context(self, length):
                self.__context = self.__context[:length]

        harry_potter_book = Document('Harry Potter', 'J. K. Rowling',
                                     '... Forever Do not believe any thing is capable of thinking'
                                     ' independently ...')

        print(harry_potter_book.title)
        print(harry_potter_book.author)
        print(harry_potter_book.get_context_length())

        harry_potter_book.intercept_context(10)

        print(harry_potter_book.get_context_length())

        print(harry_potter_book.__context)

        ########## 输出 ##########

        # init function called Harry Potter J.K.Rowling 77 10
        # ---------------------------------------------------------------------------
        # AttributeErrorTraceback(most recent call last)
        # < ipython - input - 5 - b4d048d75003 > in < module > ()
        # 22
        print(harry_potter_book.get_context_length())  # 23 ---> 24
        print(harry_potter_book.__context)

        # AttributeError: 'Document' object has no attribute '__context'

    def understand_OOP1(self):
        class Document():
            WELCOME_STR = 'Welcome! The context for this book is {}.'

            def __init__(self, title, author, context):
                print('init function called')
                self.title = title
                self.author = author
                self.__context = context

            # 类函数
            @classmethod
            def create_empty_book(cls, title, author):
                return cls(title=title, author=author, context='nothing')

            # 成员函数
            def get_context_length(self):
                return len(self.__context)

            # 静态函数
            @staticmethod
            def get_welcome(context):
                return Document.WELCOME_STR.format(context)

        empty_book = Document.create_empty_book(
            'What Every Man Thinks About Apart from Sex',
            'Professor Sheridan Simove')

        print(empty_book.get_context_length())
        print(empty_book.get_welcome('indeed nothing'))

        ########## 输出 ##########

        # init function called 7
        # Welcome! The context for this book is indeed nothing.

    def understand_OOP_Extend(self):
        class Entity():
            def __init__(self, object_type):
                print('parent class init called')
                self.object_type = object_type

            def get_context_length(self):
                raise Exception('get_context_length not implemented')

            def print_title(self):
                print(self.title)

        class Document(Entity):
            def __init__(self, title, author, context):
                print('Document class init called')
                Entity.__init__(self, 'document')
                self.title = title
                self.author = author
                self.__context = context

            def get_context_length(self):
                return len(self.__context)

        class Video(Entity):
            def __init__(self, title, author, video_length):
                print('Video class init called')
                Entity.__init__(self, 'video')
                self.title = title
                self.author = author
                self.__video_length = video_length

            def get_context_length(self):
                return self.__video_length

        harry_potter_book = Document('Harry Potter(Book)', 'J. K. Rowling',
                                     '... Forever Do not believe any thing'
                                     ' is capable of thinking independently ...')
        harry_potter_movie = Video('Harry Potter(Movie)', 'J. K. Rowling', 120)

        print(harry_potter_book.object_type)
        print(harry_potter_movie.object_type)

        harry_potter_book.print_title()
        harry_potter_movie.print_title()

        print(harry_potter_book.get_context_length())
        print(harry_potter_movie.get_context_length())

        ########## 输出 ##########

        # Document class init called
        # parent class init called
        # Video class init called
        # parent class init called
        # document
        # video
        # Harry Potter(Book)
        # Harry Potter(Movie)
        # 77
        # 120

    def understand_OOP_Extend2(self):
        from abc import ABCMeta, abstractmethod

        class Entity(metaclass=ABCMeta):
            @abstractmethod
            def get_title(self):
                pass

            @abstractmethod
            def set_title(self, title):
                pass

        class Document(Entity):
            def get_title(self):
                return self.title

            def set_title(self, title):
                self.title = title

        document = Document()
        document.set_title('Harry Potter')
        print(document.get_title())

        entity = Entity()

        ########## 输出 ##########
        # Harry Potter
        # Traceback (most recent call last):
        #   File "C:/Users/yuwzhang/Yuwzhang_Management/700-Application.Project/702-Python/ARTS/python_object_oriented-1.py", line 233, in <module>
        #     study_OOP.understand_OOP_Extend2()
        #   File "C:/Users/yuwzhang/Yuwzhang_Management/700-Application.Project/702-Python/ARTS/python_object_oriented-1.py", line 218, in understand_OOP_Extend2
        #     entity = Entity()
        # TypeError: Can't instantiate abstract class Entity with abstract methods get_title, set_title

    @staticmethod
    def understand_init_sequence_in_extend():
        class A():
            def __init__(self):
                print('enter A')
                print('leave A')

        class B(A):
            def __init__(self):
                print('enter B')
                super().__init__()
                print('leave B')

        class C(A):
            def __init__(self):
                print('enter C')
                super().__init__()
                print('leave C')

        class D(B, C):
            def __init__(self):
                print('enter D')
                super().__init__()
                print('leave D')

        D()
        D.mro()

    def change_string_representation_of_the_object(self):
        # To change the string representation of an instance, redefine its
        # __str__() and __repr__() methods
        class Pair:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            # The  __repr__() method returns the code representation of an
            #  instance
            def __repr__(self):
                return 'Pair({0.x!r}, {0.y!r})'.format(self)

            # The __str__() method converts the instance to a string
            def __str__(self):
                return '({0.x!s}, {0.y!s})'.format(self)

        p = Pair(3, 4)
        p  # Pair(3, 4) # __repr__() output
        print(p)  # (3, 4) # __str__() output

        # 使用 !r 在 print 中格式化代码，输出的内容是 __repr__ 而不是 __str__()
        print('p is {0!r}'.format(p))  # p is Pair(3, 4)
        print('p is {0}'.format(p))  # print('p is {0}'.format(p))

        # __repr__() 生成的文本字符串标准做法是需要让 eval(repr(x)) == x 为真。
        #  如果实在不能这样子做，应该创建一个有用的文本表示，并使用 < 和 > 括起来。比如：
        # >>> f = open('file.dat')
        # >>> f
        # <_io.TextIOWrapper name='file.dat' mode='r' encoding='UTF-8'>
        # >>>

        # 如果 __str__() 没有被定义，那么就会使用 __repr__() 来代替输出。

        # 上面的 format() 方法的使用看上去很有趣，格式化代码 {0.x} 对应的是第1个参数
        # 的x属性。 因此，在下面的函数中，0实际上指的就是 self 本身：

        def __repr__(self):
            return 'Pair({0.x!r}, {0.y!r})'.format(self)

        # 作为这种实现的一个替代，你也可以使用 % 操作符，就像下面这样：
        def __repr__(self):
            return 'Pair(%r, %r)' % (self.x, self.y)

    def let_an_object_support_custom_formatting(self):
        _formats = {
            'ymd': '{d.year}-{d.month}-{d.day}',
            'mdy': '{d.month}/{d.day}/{d.year}',
            'dmy': '{d.day}/{d.month}/{d.year}'
        }

        class Date:
            def __init__(self, year, month, day):
                self.year = year
                self.month = month
                self.day = day

            def __format__(self, code):
                if code == '':
                    code = 'ymd'
                fmt = _formats[code]
                return fmt.format(d=self)

        d = Date(2012, 12, 21)
        print(format(d))
        print(format(d, 'mdy'))
        print('The date is {:ymd}'.format(d))
        print('The date is {:mdy}'.format(d))

        # __format__() 方法给Python的字符串格式化功能提供了一个钩子。 这里需要着重强调的
        # 是格式化代码的解析工作完全由类自己决定。因此，格式化代码可以是任何值。
        #  例如，参考下面来自 datetime 模块中的代码：
        from datetime import date
        d = date(2012, 12, 21)
        print(format(d))
        print(format(d,'%A, %B %d, %Y'))
        print('The end is {:%d %b %Y}. Goodbye'.format(d))

    def let_object_support_the_context_management_protocol(self):
        # In order for an object to be compatible with the with statement, you
        # need to implement the __enter__() and __exit__() methods.
        from socket import socket, AF_INET, SOCK_STREAM

        class LazyConnection:
            def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
                self.address = address
                self.family = family
                self.type = type
                self.sock = None

            def __enter__(self):
                if self.sock is not None:
                    raise RuntimeError('Already connected')
                self.sock = socket(self.family, self.type)
                self.sock.connect(self.address)
                return self.sock

            def __exit__(self, exc_ty, exc_val, tb):
                self.sock.close()
                self.sock = None

        # 这个类的关键特点在于它表示了一个网络连接，但是初始化的时候并不会做任何事情(比如它
        # 并没有建立一个连接)。 连接的建立和关闭是使用 with 语句自动完成的，例如：
        from functools import partial

        conn = LazyConnection(('www.python.org', 80))
        # Connection closed
        with conn as s:
            # conn.__enter__() executes: connection open
            s.send(b'GET /index.html HTTP/1.0\r\n')
            s.send(b'Host: www.python.org\r\n')
            s.send(b'\r\n')
            resp = b''.join(iter(partial(s.recv, 8192), b''))
            # conn.__exit__() executes: connection closed

        # 编写上下文管理器的主要原理是你的代码会放到 with 语句块中执行。 当出现 with 语
        # 句的时候，对象的 __enter__() 方法被触发， 它返回的值(如果有的话)会被赋值给 as
        # 声明的变量。然后，with 语句块里面的代码开始执行。 最后，__exit__() 方法被触发
        # 进行清理工作。

        # 不管 with 代码块中发生什么，上面的控制流都会执行完，就算代码块中发生了异常也是
        # 一样的。 事实上，__exit__() 方法的第三个参数包含了异常类型、异常值和追溯信息
        # (如果有的话)。 __exit__() 方法能自己决定怎样利用这个异常信息，或者忽略它并返回
        # 一个None值。 如果 __exit__() 返回 True ，那么异常会被清空，就好像什么都没发生
        # 一样， with 语句后面的程序继续在正常执行。

        # 还有一个细节问题就是 LazyConnection 类是否允许多个 with 语句来嵌套使用连接。
        # 很显然，上面的定义中一次只能允许一个socket连接，如果正在使用一个socket的时候又
        # 重复使用 with 语句， 就会产生一个异常了。不过你可以像下面这样修改下上面的实现来
        # 解决这个问题：

        from socket import socket, AF_INET, SOCK_STREAM

        class LazyConnection:
            def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
                self.address = address
                self.family = family
                self.type = type
                self.connections = []

            def __enter__(self):
                sock = socket(self.family, self.type)
                sock.connect(self.address)
                self.connections.append(sock)
                return sock

            def __exit__(self, exc_ty, exc_val, tb):
                self.connections.pop().close()

        # Example use
        from functools import partial
        conn = LazyConnection(('www.python.org', 80))
        with conn as s1:
            pass
            with conn as s2:
                pass
                # s1 and s2 are independent sockets

        # 在第二个版本中，LazyConnection 类可以被看做是某个连接工厂。在内部，一个列表被用
        # 来构造一个栈。 每次 __enter__() 方法执行的时候，它复制创建一个新的连接并将其加
        # 入到栈里面。 __exit__() 方法简单的从栈中弹出最后一个连接并关闭它。 这里稍微有点
        # 难理解，不过它能允许嵌套使用 with 语句创建多个连接，就如上面演示的那样。

        # 在需要管理一些资源比如文件、网络连接和锁的编程环境中，使用上下文管理器是很普遍的。
        # 这些资源的一个主要特征是它们必须被手动的关闭或释放来确保程序的正确运行。 例如，如
        # 果你请求了一个锁，那么你必须确保之后释放了它，否则就可能产生死锁。
        # 通过实现 __enter__() 和 __exit__() 方法并使用 with 语句可以很容易的避免这些
        # 问题， 因为 __exit__() 方法可以让你无需担心这些了。


if __name__ == '__main__':
    # traverse_all_property_in_class()
    # support_many_operators()

    study_OOP = StudyOOP()
    # study_OOP.understand_OOP()
    # study_OOP.understand_OOP1()
    # study_OOP.understand_OOP_Extend()
    # study_OOP.understand_OOP_Extend2()
    # study_OOP.understand_init_sequence_in_extend()
    # study_OOP.change_string_representation_of_the_object()
    # study_OOP.let_an_object_support_custom_formatting()
    study_OOP.let_object_support_the_context_management_protocol()
