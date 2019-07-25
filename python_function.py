# Question1: cCreate a function that accepts any number of arguments
def create_a_funcaton_that_acceptes_any_number_of_argements():
    # Using * 接受不带默认值的参数
    def avg(first, *rest):
        return (first + sum(rest)) / (1 + len(rest))

    # Sample use
    avg(1, 2)  # 1.5
    avg(1, 2, 3, 4)  # 2.5

    # 使用 ** 接受带默认值的参数
    import html

    def make_element(name, value, **attrs):
        keyvals = [' %s="%s"' % item for item in attrs.items()]
        attr_str = ''.join(keyvals)
        element = '<{name}{attrs}>{value}</{name}>'.format(
            name=name,
            attrs=attr_str,
            value=html.escape(value))
        return element

    # Example
    # Creates '<item size="large" quantity="6">Albatross</item>'
    make_element('item', 'Albatross', size='large', quantity=6)

    # Creates '<p>&lt;spam&gt;</p>'
    make_element('p', '<spam>')

    # 在这里，attrs是一个包含所有被传入进来的关键字参数的字典。
    # 如果你还希望某个函数能同时接受任意数量的位置参数和关键字参数，可以同时使用 * 和 **。
    # 比如
    def anyargs(*args, **kwargs):
        print(args)  # A tuple
        print(kwargs)  # A dict

    # 一个*参数只能出现在函数定义中最后一个位置参数后面，而 **参数只能出现在最后一个参数。
    # 有一点要注意的是，在*参数后面仍然可以定义其他参数。
    def a(x, *args, y):
        pass

    def b(x, *args, y, **kwargs):
        pass


# Question2: A function that accepts only keyword arguments
def create_a_funcation_that_accepts_only_keyword_arguments():
    # 你希望函数的某些参数强制使用关键字参数传递
    # 将强制关键字参数放到某个*参数或者单个*后面就能达到这种效果。比如：
    # 这里强制使用 block
    def recv(maxsize, *, block):
        'Receives a message'
        pass

    recv(1024, True)  # TypeError
    recv(1024, block=True)  # Ok

    # 利用这种技术，我们还能在接受任意多个位置参数的函数中指定关键字参数。比如：
    def minimum(*values, clip=None):
        m = min(values)
        if clip is not None:
            m = clip if clip > m else m
        return m

    minimum(1, 5, 2, -5, 10)  # Returns -5
    minimum(1, 5, 2, -5, 10, clip=0)  # Returns 0

    # 很多情况下，使用强制关键字参数会比使用位置参数表意更加清晰，程序也更加具有可读性。
    # 例如，考虑下如下一个函数调用：
    msg = recv(1024, False)
    # 如果调用者对recv函数并不是很熟悉，那他肯定不明白那个False参数到底来干嘛用的。
    # 但是，如果代码变成下面这样子的话就清楚多了：
    msg = recv(1024, block=False)

    # 另外，使用强制关键字参数也会比使用**kwargs参数更好，
    # 因为在使用函数help的时候输出也会更容易理解：
    help(recv)
    # Help on function recv in module __main__:
    # recv(maxsize, *, block)
    # Receives a message


# Question3: Add meta information to function parameters
def add_meta_information_to_function_parameters():
    # 使用函数参数注解是一个很好的办法，它能提示程序员应该怎样正确使用这个函数。
    #  例如，下面有一个被注解了的函数：
    def add(x: int, y: int) -> int:
        return x + y
    # python解释器不会对这些注解添加任何的语义。它们不会被类型检查，运行时跟没有加注解之前
    # 的效果也没有任何差距。 然而，对于那些阅读源码的人来讲就很有帮助啦。
    # 第三方工具和框架可能会对这些注解添加语义。同时它们也会出现在文档中。
    help(add)
    # Help on function add in module __main__:
    # add(x: int, y: int) -> int
    # 函数注解只存储在函数的 __annotations__ 属性中。例如：
    add.__annotations__
    # {'y': <class 'int'>, 'return': <class 'int'>, 'x': <class 'int'>}


# Question4: return a function with multiple values
def return_a_function_with_multiple_values():
    def myfun():
        return 1, 2, 3
    a, b, c = myfun()
    # 看起来元组返回了多个值，实际上先创建了一个元组后返回的。
    print(a, b, c)
    x = myfun()
    print(x)


# Question5: Define a function with default parameters
def define_a_function_with_default_parameters():
    def spam(a, b=42):
        print(a, b)

    spam(1)  # Ok. a=1, b=42
    spam(1, 2)  # Ok. a=1, b=2
    # 如果默认的参数是一个可修改的容器，比如一个列表或者字典，可以使用 None 作为默认值
    # Using a list as a default value
    def spam(a, b=None):
        if b is None:
            b = []

    # 如果不想提供默认值，仅仅测试某个默认参数是不是有传递进来：
    _no_value = object()
    def spam(a, b=_no_value):
        if b is _no_value:
            print('No b value supplied')
    spam(1)
    spam(1, 2)
    spam(1, None)

    # In-depth
    # 默认的参数仅在函数定义时赋值一次
    x = 42
    def spam(a, b=x):
        print(a, b)

    spam(1)
    x = 23  # Has no effect
    spam(1)

    # 默认参数应该是不可变的对象，如None、True、False、数字或字符串
    # 千万不要这样写：
    def spam(a, b=[]):  # NO!
        print(b)
        return b
    x = spam(1)
    print(x)  # []
    x.append(99)
    x.append('Yow!')
    print(x)  # [99, 'Yow!']
    spam(1)  # [99, 'Yow!'] Modified list gets returned!

    # 好是将默认值设为None， 然后在函数里面检查它，前面的例子就是这样做的。

    # 在测试None值时使用 is 操作符是很重要的，也是这种方案的关键点。
    # 有时候大家会犯下下面这样的错误：
    def spam(a, b=None):
        if not b:  # NO! Use 'b is None' instead
            b = []
    # 这么写的问题在于尽管None值确实是被当成False， 但是还有其他的对象(比如长度为0的字符串
    # 、列表、元组、字典等)都会被当做False。 因此，上面的代码会误将一些其他输入也当成是
    # 没有输入。比如：
    spam(1)  # OK
    x = []
    spam(1, x)  # Silent error. x value overwritten by default
    spam(1, 0)  # Silent error. 0 ignored
    spam(1, '')  # Silent error. '' ignored

    # 有些时候那就是一个函数需要测试某个可选参数是否被使用者传递进来。 这时候需要小心的是你
    # 不能用某个默认值比如None、 0或者False值来测试用户提供的值(因为这些值都是合法的值，
    # 是可能被用户传递进来的)。

    # 为了解决这个问题，你可以创建一个独一无二的对象实例，在函数里面，你可以通过检查被传递
    # 参数值跟这个实例是否一样来判断。

    # 这里对 object() 的使用看上去有点不太常见。object 是python中所有类的基类。
    # 你可以创建 object 类的实例，但是这些实例没什么实际用处，因为它并没有任何有用的方法，
    # 也没有任何实例数据(因为它没有任何的实例字典，你甚至都不能设置任何属性值)。


if __name__ == "__main__":

    # create_a_funcaton_that_acceptes_any_number_of_argements()
    # create_a_funcation_that_accepts_only_keyword_arguments()
    # add_meta_information_to_function_parameters()
    # return_a_function_with_multiple_values()
    define_a_function_with_default_parameters()


