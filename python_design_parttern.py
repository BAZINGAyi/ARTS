

# Question1: 实现单例模式
# 使用装饰器

def decorator_method():

    def singleton(cls):
        instances = {}

        def wrapper(*args, **kwargs):
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
            return instances[cls]
        return wrapper

    @singleton
    class Foo(object):
        pass

    foo1 = Foo()
    foo2 = Foo()
    print(foo1 is foo2)  # True


# 使用正常类创建对象的方法
def class_method():
    class Singleton(object):
        def __new__(cls, *args, **kwargs):
            if not hasattr(cls, '_instance'):
                cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            return cls._instance

    class Foo(Singleton):
        pass

    foo1 = Foo()
    foo2 = Foo()
    print(foo1 is foo2)  # True


# 元类方法
def metaclass_method():
    class Singleton(type):
        def __call__(cls, *args, **kwargs):
            if not hasattr(cls, '_instance'):
                cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instance

    # Python2
    # class Foo(object):
    #     __metaclass__ = Singleton

    # Python3
    class Foo(metaclass=Singleton):
        pass

    foo1 = Foo()
    foo2 = Foo()
    print(foo1 is foo2)  # True


if __name__ == '__main__':
    decorator_method()

    class_method()

    metaclass_method()