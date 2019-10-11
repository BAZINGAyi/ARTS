class StudyThread(object):

    @staticmethod
    def start_a_thread():
        """
        start() -> 开始执行线程
        is_alive() -> 判断线程的有运行状态
        join() -> 等待调用此方法的进程结束
        :return:
        """
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

        如果设置为 daemon thread，主线程不会等待 daemon 线程，只要所有非
        daemon thread 退出后，main 就会退出，并且回收资源。
        :return:
        """

        import time
        from threading import Thread

        def countdown(n):
            while n > 0:
                print('T-minus', n)
                n -= 1
                time.sleep(1)

        t = Thread(target=countdown, args=(10,))
        # True: 子进程不会执行完成，就会和主线程一起退出
        # False: 主线程会等子线程完成后再退出
        t.setDaemon(True)
        t.start()
        print('main thread is over')

    @staticmethod
    def scheduling_a_thread():
        """
        Dynamically shutting down running threads
        :return:
        """
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
                    import time
                    time.sleep(5)

        c = CountdownTask()
        t = Thread(target=c.run, args=(10,))
        t.start()
        c.terminate()  # Signal termination
        # Will wait for the thread to continue running for 5s and then exit
        t.join()  # Wait for actual termination (if needed)

    @staticmethod
    def scheduling_a_io_thread():
        """
        如果线程执行一些 I/O 这样的阻塞操作，并阻塞在一个操作上，就无法返回，也就无法检查
        自己被结束了，需要使用超时来小心操作线程
        :return:
        """
        from socket import AF_INET, SOCK_STREAM

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
                        print(str(e))
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

    @staticmethod
    def get_the_state_of_a_running_thread():
        """
        Question: 线程同步(通信)问题
        线程的一个关键特性是每个线程都是独立运行且状态不可预测。
        如果程序中的其他线程需要通过判断某个线程的状态来确定自己下一步的操作，这时线程同步
        问题就会变得非常棘手。

        Answer:
        为了解决这些问题，我们需要使用 threading 库中的 Event 对象。 Event 对象
        包含一个可由线程设置的信号标志，它允许线程等待某些事件的发生。

        event 对象的特定点是当被设置为真时，会唤醒所有等待它的线程。

        Notice:
        event 对象最好单次使用，在创建 event 对象后，让某个线程等待这个对象，一旦这个对象
        被设置为真，就应该丢弃它。尽管可以通过 clear() 方法来重置 event，但很难保证安全地
        清理 event 对象，很可能发生错过时间，死锁或者其他问题(无法保证重置 event 对象的
        代码会在线程再次等待这个 event 对象之前执行)

        如果一个线程不停需要重复使用 event 对象，最好使用 Condition 对象来代替。
        :return:
        """
        from threading import Thread, Event
        import time

        # Code to execute in an independent thread
        def countdown(n, started_evt: Event):
            started_evt.wait()
            print('countdown starting')
            while n > 0:
                print('T-minus', n)
                n -= 1
                time.sleep(2)

        # Create the event object that will be used to signal startup
        started_evt = Event()

        # Launch the thread and pass the startup event
        print('Launching countdown')
        t = Thread(target=countdown, args=(10, started_evt))
        t.start()
        # 在主线程 sleep 5s 后，启动子线程
        time.sleep(5)
        started_evt.set()
        # Wait for the thread to start
        print('countdown is running')

    @staticmethod
    def thread_synchronization_problem_by_condition():
        """
        下面的例子中 PeriodTimer 中作为线程间的控制器，每当 Condition 发生变化时，
        countdown 和 countup 两个线程运行并计算
        :return:
        """
        import threading
        import time

        class PeriodicTimer:
            def __init__(self, interval):
                self._interval = interval
                self._flag = 0
                self._cv = threading.Condition()

            def start(self):
                t = threading.Thread(target=self.run)
                t.daemon = True
                t.start()

            def run(self):
                '''
                Run the timer and notify waiting threads after each interval
                '''
                while True:
                    time.sleep(self._interval)
                    with self._cv:
                        self._flag ^= 1
                        self._cv.notify_all()

            def wait_for_tick(self):
                '''
                Wait for the next tick of the timer
                '''
                with self._cv:
                    last_flag = self._flag
                    while last_flag == self._flag:
                        self._cv.wait()

        # Example use of the timer
        ptimer = PeriodicTimer(5)
        ptimer.start()

        # Two threads that synchronize on the timer
        def countdown(nticks):
            while nticks > 0:
                ptimer.wait_for_tick()
                print('T-minus', nticks)
                nticks -= 1

        def countup(last):
            n = 0
            while n < last:
                ptimer.wait_for_tick()
                print('Counting', n)
                n += 1

        threading.Thread(target=countdown, args=(10,)).start()
        threading.Thread(target=countup, args=(5,)).start()

    @staticmethod
    def thread_synchronization_problem_by_sema():
        """
         Question: event对象的一个重要特点是当它被设置为真时会唤醒所有等待它的线程。
        如果你只想唤醒单个线程，最好是使用信号量或者 Condition 对象来替代.

        这是因为所有的线程都在等待获取信号量。每次信号量被释放，只有一个线程会被唤醒并执行.
        :return:
        """
        import threading

        # Worker thread
        def worker(n, sema):
            # Wait to be signaled
            sema.acquire()

            # Do some work
            print('Working', n)

        # Create some threads
        sema = threading.Semaphore(0)
        nworkers = 10
        for n in range(nworkers):
            t = threading.Thread(target=worker, args=(n, sema,))
            t.start()

        # 线程被唤醒的顺序与线程启动时的顺序无关
        sema.release()
        sema.release()
        sema.release()


class ProducerAndConsumerModel(object):
    @staticmethod
    def production_consumption_model_realized_by_queue():
        """
        Question: 在多个线程中，安全地交换信息或者数据

        Answer: 使用 Queue 对象，在多个线程中共享，使用 put() 或者
         get() 来添加或者删除元素. 注意 put 和 get 的阻塞情况
        """

        from queue import Queue
        from threading import Thread

        # A thread that produces data
        def producer(out_q):
            while True:
                # Produce some data
                data = [1, 2, 3]
                out_q.put(data)

        # A thread that consumes data
        def consumer(in_q):
            while True:
                # Get some data
                data = in_q.get()
                # Process the data
                print(data)

        # Create the shared queue and launch both threads
        q = Queue()
        t1 = Thread(target=consumer, args=(q,))
        t2 = Thread(target=producer, args=(q,))
        t1.start()
        t2.start()

    @staticmethod
    def the_close_problem_of_production_consumption_model():
        """
        根据一些条件来关闭生产者和消费者.

        通过设置一个特殊值，其中一个消费者读到这个值后，把这个特殊值再次放到队列中，然后将
        自己关闭，这样所有监听这个队列的消费者线程都可以全部关闭了
        :return:
        """

        from queue import Queue
        from threading import Thread

        # Object that signals shutdown
        _sentinel = object()

        # A thread that produces data
        def producer(out_q):
            count = 10
            data = []
            while count > 0:
                # Produce some data
                import copy
                data.append(count)
                data_copy = copy.deepcopy(data)
                out_q.put(data_copy)
                count -= 1

            # Put the sentinel on the queue to indicate completion
            out_q.put(_sentinel)

        # A thread that consumes data
        def consumer(in_q, consumer_name):
            while True:
                # Get some data
                data = in_q.get()

                # Check for termination
                if data is _sentinel:
                    in_q.put(_sentinel)
                    print(consumer_name + ': closed consumer')
                    break
                else:
                    # Process data
                    print(consumer_name + ':', data)

                # Proc

        q = Queue()
        c1 = Thread(target=consumer, args=(q, 'consumer_name1'))
        c2 = Thread(target=consumer, args=(q, 'consumer_name2'))
        p1 = Thread(target=producer, args=(q,))
        c1.start()
        c2.start()
        p1.start()

    @staticmethod
    def implements_a_thread_safe_priority_queue():
        """
        Question: 手动实现一个线程安全的优先队列
        Answer: 使用 Condition 来包装数据结构
        :return:
        """
        import heapq
        import threading

        class PriorityQueue:
            def __init__(self):
                self._queue = []
                self._count = 0
                self._cv = threading.Condition()

            def put(self, item, priority):
                with self._cv:
                    heapq.heappush(self._queue, (-priority, self._count, item))
                    self._count += 1
                    self._cv.notify()

            def get(self):
                with self._cv:
                    while len(self._queue) == 0:
                        self._cv.wait()
                    return heapq.heappop(self._queue)[-1]

        from threading import Thread

        # A thread that produces data
        def producer(out_q):
            priority = 10
            data = []
            while priority > 0:
                # Produce some data
                import copy
                data.append(priority)
                data_copy = copy.deepcopy(data)
                out_q.put(data_copy, priority)
                priority -= 1

        # A thread that consumes data
        def consumer(in_q):
            while True:
                # Get some data
                data = in_q.get()
                # Process the data
                print(data)

        priorityQueue = PriorityQueue()
        t1 = Thread(target=consumer, args=(priorityQueue,))
        t2 = Thread(target=producer, args=(priorityQueue,))
        t2.start()
        t1.start()

    @staticmethod
    def indicates_the_status_of_the_queue_completion():
        """
        等待所有的产生的数据都被消费完
        :return:
        """
        from queue import Queue
        from threading import Thread

        # A thread that produces data
        def producer(out_q, sleep_time):
            priority = 10
            data = []
            while priority > 0:
                # Produce some data
                import copy
                data.append(priority)
                data_copy = copy.deepcopy(data)
                out_q.put(data_copy)
                priority -= 1
                import time
                time.sleep(sleep_time)

        # A thread that consumes data
        def consumer(in_q):
            while True:
                # Get some data
                data = in_q.get()
                # Process the data
                print(data)
                # Indicate completion
                in_q.task_done()

        # Create the shared queue and launch both threads
        q = Queue()
        p1 = Thread(target=producer, args=(q, 0))
        p2 = Thread(target=producer, args=(q, 2))
        c1 = Thread(target=consumer, args=(q,), daemon=True)
        p1.start()
        p2.start()
        c1.start()

        # wait for all producer to end
        p1.join()
        p2.join()

        # Wait for all produced items to be consumed
        q.join()


class ThreadDemo(object):
    @staticmethod
    def single_thread_download():
        """
        单线程下载 wiki 并记录时间
        :return:
        """
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
    def download_and_process_data_at_the_same_time():

        import requests
        import time
        from threading import Thread

        def print_safe(data):
            import threading
            mutex = threading.Lock()
            mutex.acquire()
            print(data)
            mutex.release()

        def download_one(url_queue, result_queue):
            while True:
                download_url = url_queue.get()
                resp = requests.get(download_url)
                print_safe('Read {} from {}'.format(
                    len(resp.content), download_url))
                result_queue.put(resp.content)
                # task_done must be placed at the end
                url_queue.task_done()

        def process_one(result_queue):
            while True:
                data = result_queue.get()
                print('process: ' + str(len(data)))
                result_queue.task_done()

        def start_download_all_sites(num_fetch_threads, url_queue, result_queue):
            for i in range(num_fetch_threads):
                worker = Thread(target=download_one,
                                args=(url_queue, result_queue), daemon=True)
                worker.start()

        def process_all_data(num_process_threads, result_queue):
            for i in range(num_process_threads):
                worker = Thread(target=process_one,
                                args=(result_queue,), daemon=True)
                worker.start()

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
            from queue import Queue
            url_queue = Queue()
            result_queue = Queue()
            start_time = time.perf_counter()
            # put all object sites to queue
            for site in sites:
                url_queue.put(site)
            print(url_queue.qsize())
            #
            start_download_all_sites(5, url_queue, result_queue)
            #
            process_all_data(5, result_queue)

            # 等待所有的 url 都被下载完成
            url_queue.join()

            # 等待所有的下载内容都被处理
            result_queue.join()

            end_time = time.perf_counter()

            print('Download {} sites in {} seconds'.format(
                len(sites), end_time - start_time))

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

    @staticmethod
    def multi_thread_download():
        import concurrent.futures
        import requests
        import time

        def download_one(url):
            # requests.get() 是线程安全的
            resp = requests.get(url)
            print('Read {} from {}'.format(len(resp.content), url))

        def download_all(sites):
            with concurrent.futures.ThreadPoolExecutor(
                    max_workers=5) as executor:
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

    # python2 中，保证线程安全的队列使用
    # python2_thread = Python2Thread()
    # python2_thread.thread_and_queue()

    """
    ############ 以下均为 Python3 中线程的使用 ##########
    """
    # 线程的基本使用 join, is_alive, start 等方法
    # StudyThread.start_a_thread()

    # python 开启 daemon 线程，daemon 线程会随着主线程的关闭而关闭
    # StudyThread.start_a_daemon_thread()

    # 单线程下载 wiki, 并测量下载时间
    # StudyThread.single_thread_download()

    # 手动的关闭正在运行的线程
    # StudyThread.scheduling_a_thread()

    # 调度一个可阻塞的 IO 线程, 设置超时时间
    # StudyThread.scheduling_a_io_thread()

    # 使用 event 对象来解决线程间依赖的问题，比如 A 线程需要等 B 线程通知后再运行
    # StudyThread.get_the_state_of_a_running_thread()

    # 使用 Condition 对象来解决需要重复通知线程执行的问题，比如 A 线程会周期的通知 B
    # 线程执行
    # StudyThread.thread_synchronization_problem_by_condition()

    # 使用信号量每次唤醒单个线程，比如 A 线程通知后,B,C 随机线程选择一个执行
    # StudyThread.thread_synchronization_problem_by_sema()

    # 多线程间通信 - Queue - 生产消费模型1: 同时产生和消费数据，
    # 保持运行：P 和 C 为正常线程
    # ProducerAndConsumerModel.production_consumption_model_realized_by_queue()

    # Queue - 通过设置一些特殊值，来关闭所有的消费者
    # ProducerAndConsumerModel.the_close_problem_of_production_consumption_model()

    # Queue - 实现线程安全的优先队列
    # ProducerAndConsumerModel.implements_a_thread_safe_priority_queue()

    # Queue - 生产消费模型2: 待生产的数据已知，可以直接使用 queue.join 来判定任务的完成
    # ThreadDemo.download_and_process_data_at_the_same_time()

    # Queue - 生产消费模型3: 带生产的数据未知，同时产生和消费数据，根据特定的条件结束
    # 1. 消费的速度大于生产的速度，使用 producer.join 来保证所有的生产任务已经完成。
    # 否则就会出现新的任务还没加到队列中，queue.join 无法被阻塞的情况，致使任务退出
    # 2. 生产大于消费的速度，同样给队列设置上限，到达上限生产者被阻塞，等待消费者完成
    # 后再发送
    # ProducerAndConsumerModel.indicates_the_status_of_the_queue_completion()

    # 使用多线程下载多个任务并使用多线程消费，使用 queue
    # 生产消费问题1： 多个生产者先产生所有数据，多个消费者进行消费，然后结束：
    # p 为正常线程 c 和 daemon 线程，使用 q.join 和 q.task_done 来表明任务已经完成

    # 生产消费问题2： 同时产生和消费数据，保持运行：P 和 C 为正常线程

    # 生产消费问题3： 同时产生和消费数据，根据特定的条件结束
    # 消费的速度大于生产的速度，使用 q.join 来判断时所有的任务已经完成，
    # 但新的任务还没加到队列中，指示任务退出. 所以需要等待所有的生产者结束
    # 生产大于消费的速度，同样给队列设置上限，到达上限生产者被阻塞，等待消费者完成后再发送

    # Futures 是对 threading 和 multiprocessing 的进一步抽象，
    # 使开发者只需编写少量代码即可让程序实现并行计算。
    # FuturesStudy.study_futures()
    # FuturesStudy.multi_thread_download()

    # 实际应用
    # 单线程下载网页
    # ThreadDemo.single_thread_download()

    # 多线程下载网页，多线程处理内容
    ThreadDemo.download_and_process_data_at_the_same_time()


