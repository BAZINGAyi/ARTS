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


def multi_thread_download():
    import concurrent.futures
    import requests
    import threading
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

    @ staticmethod
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


if __name__ == '__main__':

    # single_thread_download()

    # multi_thread_download()

    # FuturesStudy.study_futures()

    python2_thread = Python2Thread()
    python2_thread.thread_and_queue()
