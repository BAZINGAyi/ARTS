import multiprocessing
# multi process start
import time


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers, cpu_bound):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


# multi process end
if __name__ == '__main__':

    # multi processing start

    # 定义在模块顶级的函数才能被 pickable，如果定义在类里或者定义在嵌套函数里，
    # 注意抛出 un pickable 异常
    numbers = [10000000 + x for x in range(20)]
    start_time = time.time()
    find_sums(numbers, cpu_bound)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")

    # multi processing stop
