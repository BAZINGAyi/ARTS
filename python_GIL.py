# 使用多线程跑 CPU bound 代码，显现 GIL 问题
import time
from threading import Thread


def CountDown(n):
    while n > 0:
        n -= 1


def multi_thread_cpu_bound():
    n = 100000000
    t1 = Thread(target=CountDown, args=[n // 2])
    t2 = Thread(target=CountDown, args=[n // 2])
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def single_thread_cpu_bound():
    n = 100000000
    t1 = Thread(target=CountDown, args=[n])
    t1.start()
    t1.join()


if __name__ == '__main__':

    # Question1: GIL 让进行 CPU Bound 任务时，多线程花费的时间比单线程花费的时间更多

    # start_time = time.time()
    # single_thread_cpu_bound()
    # duration = time.time() - start_time
    # print(f"Duration {duration} seconds")  # Duration 6.916451930999756 seconds
    #
    # start_time = time.time()
    # multi_thread_cpu_bound()
    # duration = time.time() - start_time
    # print(f"Duration {duration} seconds")  # Duration 7.0152268409729 seconds

    # Question2: GIL 下并发多线程，仍然会出现 race condition 的情况，可以使用 Python2
    # 模拟
    import threading
    x = 0

    def increment_global():
        global x
        x += 1

    def taskofThread():
        for _ in range(50000):
            increment_global()

    def main():
        global x
        x = 0

        t1 = threading.Thread(target=taskofThread)
        t2 = threading.Thread(target=taskofThread)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


    for i in range(5):
        main()
        print("x = {1} after Iteration {0}".format(i, x))



