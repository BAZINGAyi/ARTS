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


if __name__ == "__main__":

    # create_a_funcaton_that_acceptes_any_number_of_argements()

    # create_a_funcation_that_accepts_only_keyword_arguments()

    # add_meta_information_to_function_parameters()

    return_a_function_with_multiple_values()