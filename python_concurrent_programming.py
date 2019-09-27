class StudyThread(object):
    @staticmethod
    def single_thread_download():
        import requests
        import time

        def download_one(url):
            resp = requests.get(url)
            print('Read {} from {}'.format(len(resp.content), url))

        def download_all(sites):
            for site in sites:
                download_one(site)

        def main():
            sites = [
                'https://en.wikipedia.org/wiki/Portal:Arts',
                'https://en.wikipedia.org/wiki/Portal:History',
                'https://en.wikipedia.org/wiki/Portal:Society',
                'https://en.wikipedia.org/wiki/Portal:Biography',
                'https://en.wikipedia.org/wiki/Portal:Mathematics',
                'https://en.wikipedia.org/wiki/Portal:Technology',
                'https://en.wikipedia.org/wiki/Portal:Geography',
                'https://en.wikipedia.org/wiki/Portal:Science',
                'https://en.wikipedia.org/wiki/Computer_science',
                'https://en.wikipedia.org/wiki/Python_(programming_language)',
                'https://en.wikipedia.org/wiki/Java_(programming_language)',
                'https://en.wikipedia.org/wiki/PHP',
                'https://en.wikipedia.org/wiki/Node.js',
                'https://en.wikipedia.org/wiki/The_C_Programming_Language',
                'https://en.wikipedia.org/wiki/Go_(programming_language)'
            ]
            start_time = time.perf_counter()
            download_all(sites)
            end_time = time.perf_counter()
            print('Download {} sites in {} seconds'.format(
                len(sites), end_time - start_time))
            # Download 15 sites in 32.088936727272724 seconds

        main()

    @staticmethod
    def start_a_thread():
        import time

        def countdown(n):
            while n > 0:
                print('T-minus', n)
                n -= 1
                time.sleep(1)

        # Create and launch a thread
        from threading import Thread
        t = Thread(target=countdown, args=(10,))
        # start running the thread
        t.start()
        #  check the status of thread running
        if t.is_alive():
            print('Still running')
        else:
            print('Completed')
        # make the main thread waiting for the son thread
        print('main thread is end')
        t.join()
        print('son thread is end')

    @staticmethod
    def start_a_daemon_thread():
        """
        daemon 可以被称为 后台线程，适用于需要长时间或者需要一直运行的任务。
        这被线程不会被等待，会在主线程终止时自动销毁。
        :return:
        """
        # 如果设置为 daemon thread，主线程不会等待 daemon 线程，只要所有非
        # daemon thread 退出后，main 就会退出，并且回收资源。
        import time
        from threading import Thread

        def countdown(n):
            while n > 0:
                print('T-minus', n)
                n -= 1
                time.sleep(1)

        t = Thread(target=countdown, args=(10,), daemon=True)
        t.start()

    @staticmethod
    def scheduling_a_thread():
        from threading import Thread

        class CountdownTask:
            def __init__(self):
                self._running = True

            def terminate(self):
                self._running = False

            def run(self, n):
                while self._running and n > 0:
                    print('T-minus', n)
                    n -= 1
                    time.sleep(5)

        c = CountdownTask()
        t = Thread(target=c.run, args=(10,))
        t.start()
        c.terminate()  # Signal termination
        t.join()  # Wait for actual termination (if needed)

    @staticmethod
    def scheduling_a_io_thread():
        """
        如果线程执行一些 I/O 这样的阻塞操作，并阻塞在一个操作上，就无法返回，也就无法检查
        自己被结束了，需要使用超时来小心操作线程
        :return:
        """
        from socket import socket, AF_INET, SOCK_STREAM

        class IOTask:
            def __init__(self):
                self._running = True

            def terminate(self):
                self._running = False

            def run(self, sock):
                import socket
                # sock is a socket
                sock.settimeout(5)  # Set timeout period
                while self._running:
                    # Perform a blocking I/O operation w/ timeout
                    try:
                        data = sock.recv(8192)
                        print(data)
                        break
                    except socket.timeout:
                        print('timeout.....')
                        continue
                    except Exception as e:
                        print(str('yuwei:111' + str(e)))
                    # Continued processing
                    ...
                # Terminated
                return

        def echo_server(address, backlog=5):
            from socket import socket
            sock = socket(AF_INET, SOCK_STREAM)
            sock.bind(address)
            sock.listen(backlog)
            print('111111')
            while True:
                client_sock, client_addr = sock.accept()
                ioTask = IOTask()
                print('222222')
                ioTask.run(client_sock)

        echo_server(('', 20000))


def multi_thread_download():
    import concurrent.futures
    import requests
    import time

    def download_one(url):
        # requests.get() 是线程安全的
        resp = requests.get(url)
        print('Read {} from {}'.format(len(resp.content), url))

    def download_all(sites):
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(download_one, sites)
        # 并行的方式一般用在 CPU heavy 的场景中，因为对于 I/O heavy 的操作，多数时间都会
        # 用于等待，相比于多线程，使用多进程并不会提升效率。反而很多时候，因为 CPU 数量的
        # 限制，会导致其执行效率不如多线程版本。
        # with futures.ProcessPoolExecutor() as executor

    def main():
        sites = [
            'https://en.wikipedia.org/wiki/Portal:Arts',
            'https://en.wikipedia.org/wiki/Portal:History',
            'https://en.wikipedia.org/wiki/Portal:Society',
            'https://en.wikipedia.org/wiki/Portal:Biography',
            'https://en.wikipedia.org/wiki/Portal:Mathematics',
            'https://en.wikipedia.org/wiki/Portal:Technology',
            'https://en.wikipedia.org/wiki/Portal:Geography',
            'https://en.wikipedia.org/wiki/Portal:Science',
            'https://en.wikipedia.org/wiki/Computer_science',
            'https://en.wikipedia.org/wiki/Python_(programming_language)',
            'https://en.wikipedia.org/wiki/Java_(programming_language)',
            'https://en.wikipedia.org/wiki/PHP',
            'https://en.wikipedia.org/wiki/Node.js',
            'https://en.wikipedia.org/wiki/The_C_Programming_Language',
            'https://en.wikipedia.org/wiki/Go_(programming_language)'
        ]
        start_time = time.perf_counter()
        download_all(sites)
        end_time = time.perf_counter()
        print('Download {} sites in {} seconds'.format(len(sites),
                                                       end_time - start_time))
        # Download 15 sites in 4.216313696969697 seconds

    main()


class FuturesStudy(object):
    """
    Futures 模块，但从Python3.2开始，标准库为我们提供了concurrent.futures模块，它提供了
    ThreadPoolExecutor 和 ProcessPoolExecutor 两个类，实现了对 threading 和
    multiprocessing 的进一步抽象，使得开发者只需编写少量代码即可让程序实现并行计算。

    用在 concurrent.futures 和 asyncio 中，表示带有延迟的操作。会将处于
    等待的操作，放到队列中，这些操作的状态可以随时查询，当完成或者出现异常时，也能在操作完
    城后被获取。

    Executor 类，执行 executor.submit(func) 时，会安排 func 执行，并返回创建好的
    future 实例，方便查询调用

    done() -> 表示操作是否完成，done() 操作不会被堵塞，会立即返回结果。

    add_done_callback(fn), 用于回调，当 Futures 完成后，fn 会被通知调用

    result() -> 当 future 完成后，返回对应的结果或者异常。

    as_completed(fs) -> 给定 future 迭代器 fs，在完成后，返回完成后的迭代器
    """

    @staticmethod
    def study_futures():
        import concurrent.futures
        import requests
        import time

        def download_one(url):
            resp = requests.get(url)
            print('Read {} from {}'.format(len(resp.content), url))
            return 'Read {} from {}'.format(len(resp.content), url)

        def download_all(sites):
            with concurrent.futures.ThreadPoolExecutor(
                    max_workers=5) as executor:
                to_do = []
                for site in sites:
                    future = executor.submit(download_one, site)
                    to_do.append(future)

                test_list = []
                for future in concurrent.futures.as_completed(to_do):
                    test_list.append(future.result())

                print(test_list.__len__())
                for i in test_list:
                    print(i)

        def main():
            sites = [
                'https://en.wikipedia.org/wiki/Portal:Arts',
                'https://en.wikipedia.org/wiki/Portal:History',
                'https://en.wikipedia.org/wiki/Portal:Society',
                'https://en.wikipedia.org/wiki/Portal:Biography',
                'https://en.wikipedia.org/wiki/Portal:Mathematics',
                'https://en.wikipedia.org/wiki/Portal:Technology',
                'https://en.wikipedia.org/wiki/Portal:Geography',
                'https://en.wikipedia.org/wiki/Portal:Science',
                'https://en.wikipedia.org/wiki/Computer_science',
                'https://en.wikipedia.org/wiki/Python_(programming_language)',
                'https://en.wikipedia.org/wiki/Java_(programming_language)',
                'https://en.wikipedia.org/wiki/PHP',
                'https://en.wikipedia.org/wiki/Node.js',
                'https://en.wikipedia.org/wiki/The_C_Programming_Language',
                'https://en.wikipedia.org/wiki/Go_(programming_language)'
            ]
            start_time = time.perf_counter()
            download_all(sites)
            end_time = time.perf_counter()
            print('Download {} sites in {} seconds'.format(len(sites),
                                                           end_time - start_time))
            # future 列表中每个 future 完成的顺序，和在列表的顺序不一定完全一致。完成
            # 的时间，取决于系统的调度和每个future 的执行时间。

        main()


class Python2Thread(object):
    @staticmethod
    def thread_and_queue():
        import threading
        from queue import Queue

        def job(l, queue):
            for i in range(len(l)):
                l[i] = l[i] ** 2
            queue.put(l)

        def multithreading():
            q = Queue()
            threads = []
            data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]
            for i in range(len(data)):
                t = threading.Thread(target=job, args=(data[i], q))
                t.start()
                threads.append(t)
            for thread in threads:
                thread.join()
            results = []

            while not q.empty():
                results.append(q.get())

            print(results)

        multithreading()


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
    studyThread = StudyThread()
    # studyThread.single_thread_download()
    # studyThread.start_a_thread()

    # python 开启 daemon 线程，daemon 线程会随着主线程的关闭而关闭
    # StudyThread.start_a_daemon_thread()

    # python 调度线程
    # StudyThread.scheduling_a_thread()

    # 调度一个可阻塞的线程
    StudyThread.scheduling_a_io_thread()

    # 调度 IO 线程


    # multi_thread_download()
    #
    # FuturesStudy.study_futures()
    #
    # python2_thread = Python2Thread()
    # python2_thread.thread_and_queue()

    # multi processing start
    # 定义在模块顶级的函数才能被 pickable，如果定义在类里或者定义在嵌套函数里，
    # 注意抛出 un pickable 异常
    # numbers = [10000000 + x for x in range(20)]
    # start_time = time.time()
    # find_sums(numbers, cpu_bound)
    # duration = time.time() - start_time
    # print(f"Duration {duration} seconds")
    # multi procesing stop
