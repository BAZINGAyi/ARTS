

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


if __name__ == '__main__':
    uses_asterisk()