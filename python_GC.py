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

    @staticmethod
    def manually_call_gc():
        import gc
        import os
        import psutil

        def show_memory_info(hint):
            pid = os.getpid()
            p = psutil.Process(pid)

            info = p.memory_full_info()
            memory = info.uss / 1024. / 1024
            print('{} memory used: {} MB'.format(hint, memory))

        show_memory_info('initial')

        a = [i for i in range(10000000)]

        show_memory_info('after a created')

        del a
        gc.collect()

        show_memory_info('finish')
        # 这里会报错证明已经将 a 回收了
        print(a)

    @staticmethod
    def understand_circular_reference_problem():
        """
        a 和 b 相互引用，并且作为局部变量，在函数 func 调用结束后，a 和 b 两个指针理论上
        已经不存在了，但依然有内存占用，因为之间的互相引用，导致引用数都不为 0
        :return:
        """
        import os
        import psutil

        def show_memory_info(hint):
            pid = os.getpid()
            p = psutil.Process(pid)

            info = p.memory_full_info()
            memory = info.uss / 1024. / 1024
            print('{} memory used: {} MB'.format(hint, memory))

        def func():
            show_memory_info('initial')
            a = [i for i in range(10000000)]
            b = [i for i in range(10000000)]
            show_memory_info('after a, b created')
            a.append(b)
            b.append(a)

        func()
        show_memory_info('finished')

    @staticmethod
    def solve_circular_reference_problem():
        import gc
        import os
        import psutil

        def show_memory_info(hint):
            pid = os.getpid()
            p = psutil.Process(pid)

            info = p.memory_full_info()
            memory = info.uss / 1024. / 1024
            print('{} memory used: {} MB'.format(hint, memory))

        def func():
            show_memory_info('initial')
            a = [i for i in range(10000000)]
            b = [i for i in range(10000000)]
            show_memory_info('after a, b created')
            a.append(b)
            b.append(a)

        func()
        gc.collect()
        show_memory_info('finished')

    @staticmethod
    def debug_circular_reference_problem():
        import objgraph

        a = [1, 2, 3]
        b = [4, 5, 6]

        a.append(b)
        b.append(a)

        objgraph.show_refs([a])
        # objgraph.show_backrefs([a])


if __name__ == '__main__':
    # 当对象的引用数量为 0 时，会被 GC 回收
    # UnderstandGC.refcount_test()

    # 当没有释放对象的引用，也就是大于 0 时，对象并不会被释放
    # UnderstandGC.error_code_refcount_test()

    # 查看对象被引用的数量
    # UnderstandGC.understand_object_reference()

    # 手动调用 GC 释放对象
    # UnderstandGC.manually_call_gc()

    # 循环引用问题, 对象之间相互引用，是否可以被垃圾回收
    # UnderstandGC.understand_circular_reference_problem()

    # 解决循环引用问题吗，手动调用 GC
    # UnderstandGC.solve_circular_reference_problem()

    # 调试发现循环引用问题
    UnderstandGC.debug_circular_reference_problem()

