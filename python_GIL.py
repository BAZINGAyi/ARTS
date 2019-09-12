# Question1: GIL 让进行 CPU Bound 任务时，多线程花费的时间比单线程花费的时间更多
def multi_thread_spend_more_time_than_single_thread_in_cpu_bound_task():
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

    start_time = time.time()
    single_thread_cpu_bound()
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")  # Duration 6.916451930999756 seconds

    start_time = time.time()
    multi_thread_cpu_bound()
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")  # Duration 7.0152268409729 seconds


# Question2: 下并发多线程，仍然会出现 race condition 的情况，可以使用 Python2
x = 0
def mock_race_condition():
    import threading

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


# Question3:
def print_number_in_order_in_3_thread():
    import threading
    import sys
    import time

    def showa():
        a = range(1, 100, 3)
        i = 0
        while True:
            lockc.acquire()  # 获取对方的锁，释放自己的锁
            print(a[i], end='|')
            i += 1
            sys.stdout.flush()  # 释放缓冲区
            locka.release()
            time.sleep(0.2)
            if i >= a.__len__():
                return

    def showb():
        a = range(2, 100, 3)
        i = 0
        while True:
            locka.acquire()
            print(a[i], end='|')
            i += 1
            sys.stdout.flush()
            lockb.release()
            time.sleep(0.2)
            if i >= a.__len__():
                return

    def showc():
        a = range(3, 100, 3)
        i = 0
        while True:
            lockb.acquire()
            print(a[i], end='|')
            i += 1
            sys.stdout.flush()
            lockc.release()
            time.sleep(0.2)
            if i >= a.__len__():
                return

    locka = threading.Lock()  # 定义3个互斥锁
    lockb = threading.Lock()
    lockc = threading.Lock()

    t1 = threading.Thread(target=showa)  # 定义3个线程
    t2 = threading.Thread(target=showb)
    t3 = threading.Thread(target=showc)

    locka.acquire()  # 先锁住a,b锁，保证先打印a
    lockb.acquire()

    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':

    # Question1: GIL 让进行 CPU Bound 任务时，多线程花费的时间比单线程花费的时间更多
    # multi_thread_spend_more_time_than_single_thread_in_cpu_bound_task()

    # Question2: GIL 下并发多线程，仍然会出现 race condition 的情况，可以使用 Python2
    # 模拟
    # mock_race_condition()
    # x = 78768 after Iteration 0
    # x = 77595 after Iteration 1
    # x = 78273 after Iteration 2
    # x = 80322 after Iteration 3
    # x = 85246 after Iteration 4

    # Question3: 3 个线程按照顺序打印 1-100
    print_number_in_order_in_3_thread()




