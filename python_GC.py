class UnderstandGC(object):

    @staticmethod
    def refcount_test():
        import os
        import psutil

        # 显示当前 python 程序占用的内存大小
        def show_memory_info(hint):
            pid = os.getpid()
            p = psutil.Process(pid)

            info = p.memory_full_info()
            memory = info.uss / 1024. / 1024
            print('{} memory used: {} MB'.format(hint, memory))

        def func():
            show_memory_info('initial')
            a = [i for i in range(10000000)]
            show_memory_info('after a created')

        func()
        show_memory_info('finished')

    @staticmethod
    def error_code_refcount_test():
        import os
        import psutil

        # 显示当前 python 程序占用的内存大小
        def show_memory_info(hint):
            pid = os.getpid()
            p = psutil.Process(pid)

            info = p.memory_full_info()
            memory = info.uss / 1024. / 1024
            print('{} memory used: {} MB'.format(hint, memory))

        def func():
            show_memory_info('initial')
            global a
            a = [i for i in range(10000000)]
            show_memory_info('after a created')

        func()
        show_memory_info('finished')


    @staticmethod
    def understand_object_reference():
        import sys
        a = []

        # 两次引用，一次来自 a，一次来自 getrefcount
        print(sys.getrefcount(a))

        def func(a):
            # 四次引用，a，python 的函数调用栈，函数参数，和 getrefcount
            print(sys.getrefcount(a))

        func(a)

        # 两次引用，一次来自 a，一次来自 getrefcount，函数 func 调用已经不存在
        print(sys.getrefcount(a))


if __name__ == '__main__':
    # 当对象的引用数量为 0 时，会被 GC 回收
    # UnderstandGC.refcount_test()

    # 当没有释放对象的引用，也就是大于 0 时，对象并不会被释放
    # UnderstandGC.error_code_refcount_test()

    # 查看对象被引用的数量
    UnderstandGC.understand_object_reference()

