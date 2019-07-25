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


if __name__ == '__main__':
    # traverse_all_property_in_class()
    # support_many_operators()

    study_OOP = StudyOOP()
    # study_OOP.understand_OOP()
    # study_OOP.understand_OOP1()
    # study_OOP.understand_OOP_Extend()
    # study_OOP.understand_OOP_Extend2()
    study_OOP.understand_init_sequence_in_extend()
