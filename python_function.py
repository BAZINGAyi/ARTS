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


# Question6: Define anonymous or inline functions
def define_anonymous_or_line_functions():
    add = lambda x, y: x + y
    print(add(2, 3))
    print(add('hello', 'boy'))

    names = ['David Beazley', 'Brian Jones',
             'Raymond Hettinger', 'Ned Batchelder']
    print(sorted(names, key=lambda name: name.split()[-1].lower()))


# Question7: Anonymous function captures variable values
def anonymous_function_captures_variable_values():
    x = 10
    a = lambda y: x + y
    x = 20
    b = lambda y: x + y
    print(a, b)
    # 这其中的奥妙在于lambda表达式中的x是一个自由变量， 在运行时绑定值，而不是定义时就绑定，
    # 这跟函数的默认值参数定义是不同的。 因此，在调用这个lambda表达式的时候，x的值是执行时的值。
    x = 15
    print(a(10))  # 25
    x = 3
    print(b(x))   # 13

    # 如果你想让某个匿名函数在定义时就捕获到值，可以将那个参数值定义成默认参数即可，
    # 就像下面这样：
    x = 10
    a = lambda y, x=x: x + y
    x = 20
    b = lambda y, x=x: x + y
    print(a(10))
    print(b(10))

    # 在这里列出来的问题是新手很容易犯的错误，有些新手可能会不恰当的使用lambda表达式。
    #  比如，通过在一个循环或列表推导中创建一个lambda表达式列表，并期望函数能在定义时就
    # 记住每次的迭代值。例如,但是实际效果是运行是n的值为迭代的最后一个值
    funcs = [lambda x: x + n for n in range(5)]
    for f in funcs:
        print(f(0))
    # 4
    # 4
    # 4
    # 4
    # 4

    funcs = [lambda x, n=n: x + n for n in range(5)]
    for f in funcs:
        print(f(0))
    # 0
    # 1
    # 2
    # 3
    # 4


# Question8: Reduce the number of parameters of the callable object
def reduce_the_number_of_parameters_of_the_callable_object():
    def spam(a, b, c, d):
        print(a, b, c, d)

    from functools import partial
    s1 = partial(spam, 1)  # a = 1
    print(s1(2, 3, 4))  # 1 2 3 4
    print(s1(4, 5, 6))  # 1 4 5 6

    s2 = partial(spam, d=42)  # d = 42
    print(s2(1, 2, 3))  # 1 2 3 42
    print(s2(4, 5, 5))  # 4 5 5 42

    s3 = partial(spam, 1, 2, d=42)  # a = 1, b = 2, d = 42
    print(s3(3))  # 1 2 3 42
    print(s3(4))  # 1 2 4 42
    print(s3(5))  # 1 2 5 42

    # 可以看出 partial() 固定某些参数并返回一个新的callable对象。这个新的 callable 接
    # 受未赋值的参数， 然后跟之前已经赋值过的参数合并起来，最后将所有参数传递给原始函数。

    # 本节要解决的问题是让原本不兼容的代码可以一起工作。下面我会列举一系列的例子。
    # 第一个例子是，假设你有一个点的列表来表示(x,y)坐标元组。 你可以使用下面的函数来计算
    # 两点之间的距离：
    points = [(1, 2), (3, 4), (5, 6), (7, 8)]
    import math
    def distance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.hypot(x2 - x1, y2 - y1)
    # 现在假设你想以某个点为基点，根据点和基点之间的距离来排序所有的这些点。 列表的 sort()
    # 方法接受一个关键字参数来自定义排序逻辑， 但是它只能接受一个单个参数的函数(distance()
    # 很明显是不符合条件的)。 现在我们可以通过使用 partial() 来解决这个问题：
    pt = (4, 3)
    points.sort(key=partial(distance, pt))
    print(points)

    # 更进一步，partial() 通常被用来微调其他库函数所使用的回调函数的参数。 例如，下面是一段
    # 代码，使用 multiprocessing 来异步计算一个结果值， 然后这个值被传递给一个接受一个
    # result值和一个可选logging参数的回调函数：
    def output_result(result, log=None):
        if log is not None:
            log.debug('Got: %r', result)

    # A sample function
    def add(x, y):
        return x + y

    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')

    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()

    # 当给 apply_async() 提供回调函数时，通过使用 partial() 传递额外的 logging 参数。
    # 而 multiprocessing 对这些一无所知——它仅仅只是使用单个值来调用回调函数。

    # 作为一个类似的例子，考虑下编写网络服务器的问题，socketserver 模块让它变得很容易。
    # 下面是个简单的echo服务器：
    from socketserver import StreamRequestHandler, TCPServer

    class EchoHandler(StreamRequestHandler):
        def handle(self):
            for line in self.rfile:
                self.wfile.write(b'GOT:' + line)

    serv = TCPServer(('', 15000), EchoHandler)
    serv.serve_forever()

    # 不过，假设你想给EchoHandler增加一个可以接受其他配置选项的 __init__ 方法。比如：
    class EchoHandler(StreamRequestHandler):
        # ack is added keyword-only argument. *args, **kwargs are
        # any normal parameters supplied (which are passed on)
        def __init__(self, *args, ack, **kwargs):
            self.ack = ack
            super().__init__(*args, **kwargs)

        def handle(self):
            for line in self.rfile:
                self.wfile.write(self.ack + line)
    # 这么修改后，我们就不需要显式地在TCPServer类中添加前缀了。
    # 但是你再次运行程序后会报类似下面的错误：
    # Exception happened during processing of request from ('127.0.0.1', 59834)
    # Traceback (most recent call last):
    # ...
    # TypeError: __init__() missing 1 required keyword-only argument: 'ack'

    # 初看起来好像很难修正这个错误，除了修改 socketserver 模块源代码或者使用某些奇怪的方法
    # 之外。 但是，如果使用 partial() 就能很轻松的解决——给它传递 ack 参数的值来初始化即可
    # ，如下：
    from functools import partial
    serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED:'))
    serv.serve_forever()

    # 在这个例子中，__init__() 方法中的ack参数声明方式看上去很有趣，其实就是声明ack为一个
    # 强制关键字参数。 关于强制关键字参数问题我们在7.2小节我们已经讨论过了，读者可以再去回顾
    # 一下。

    # 很多时候 partial() 能实现的效果，lambda表达式也能实现。比如，之前的几个例子可以使用
    # 下面这样的表达式：
    points.sort(key=lambda p: distance(pt, p))
    p.apply_async(add, (3, 4),
                  callback=lambda result: output_result(result, log))
    serv = TCPServer(('', 15000),
                     lambda *args, **kwargs: EchoHandler(*args,
                                                         ack=b'RECEIVED:',
                                                         **kwargs))
    # 这样写也能实现同样的效果，不过相比而已会显得比较臃肿，对于阅读代码的人来讲也更加难懂。
    # 这时候使用 partial() 可以更加直观的表达你的意图(给某些参数预先赋值)。


# Question9: Convert a single method class to a function
def convert_a_single_method_class_to_a_function():
    # 大多数情况下，可以使用闭包来将单个方法的类转换成函数。 举个例子，
    # 下面示例中的类允许使用者根据某个模板方案来获取到URL链接地址。
    from urllib.request import urlopen

    class UrlTemplate:
        def __init__(self, template):
            self.template = template

        def open(self, **kwargs):
            return urlopen(self.template.format_map(kwargs))

    # Example use. Download stock data from yahoo
    yahoo = UrlTemplate(
        'http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
    for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
        print(line.decode('utf-8'))

    # 这个类可以被一个更简单的函数来代替：
    def urltemplate(template):
        def opener(**kwargs):
            return urlopen(template.format_map(kwargs))

        return opener

    # Example use
    yahoo = urltemplate(
        'http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
    for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
        print(line.decode('utf-8'))

    # 大部分情况下，你拥有一个单方法类的原因是需要存储某些额外的状态来给方法使用。
    # 比如，定义UrlTemplate类的唯一目的就是先在某个地方存储模板值，
    # 以便将来可以在open()方法中使用。
    # 使用一个内部函数或者闭包的方案通常会更优雅一些。简单来讲，一个闭包就是一个函数，
    # 只不过在函数内部带上了一个额外的变量环境。闭包关键特点就是它会记住自己被定义时的环境。
    # 因此，在我们的解决方案中，opener() 函数记住了 template 参数的值，并在接下来的调用中
    # 使用它。

    # 任何时候只要你碰到需要给某个函数增加额外的状态信息的问题，都可以考虑使用闭包。
    # 相比将你的函数转换成一个类而言，闭包通常是一种更加简洁和优雅的方案。


if __name__ == "__main__":

    # create_a_funcaton_that_acceptes_any_number_of_argements()
    # create_a_funcation_that_accepts_only_keyword_arguments()
    # add_meta_information_to_function_parameters()
    # return_a_function_with_multiple_values()
    # define_a_function_with_default_parameters()
    # define_anonymous_or_line_functions()
    # anonymous_function_captures_variable_values()
    reduce_the_number_of_parameters_of_the_callable_object()


