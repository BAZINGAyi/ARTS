class AsyncioStudyPython36(object):
    @staticmethod
    def synchronous_execution_python36():
        import asyncio

        async def crawl_page(url):
            print('crawling {}'.format(url))
            sleep_time = int(url.split('_')[-1])
            await asyncio.sleep(sleep_time)
            print('OK {}'.format(url))

        async def main(urls):
            for url in urls:
                await crawl_page(url)

        from win32.timezone import now
        start = now()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(['url_1', 'url_2', 'url_3', 'url_4']))
        print('TIME: ', now() - start)
        # TIME:  0:00:10.004659

    @staticmethod
    def asynchronous_execution_python36():
        import asyncio

        async def crawl_page(url):
            print('crawling {}'.format(url))
            sleep_time = int(url.split('_')[-1])
            await asyncio.sleep(sleep_time)
            print('OK {}'.format(url))

        async def main(urls):
            tasks = [asyncio.ensure_future(crawl_page(url)) for url in urls]
            for task in tasks:
                await task
            # await asyncio.gather(*tasks)

        from win32.timezone import now
        start = now()
        loop = asyncio.get_event_loop()
        task = loop.create_task(main(['url_1', 'url_2', 'url_3', 'url_4']))
        loop.run_until_complete(task)
        print('TIME: ', now() - start)
        # TIME:  0:00:4.004659

    @staticmethod
    def the_synchronous_process():
        import asyncio

        async def worker_1():
            print('worker_1 start')
            await asyncio.sleep(1)
            print('worker_1 done')

        async def worker_2():
            print('worker_2 start')
            await asyncio.sleep(2)
            print('worker_2 done')

        async def main():
            print('before await')
            await worker_1()
            print('awaited worker_1')
            await worker_2()
            print('awaited worker_2')

        from win32.timezone import now
        start = now()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        print('TIME: ', now() - start)

        ########## 输出 ##########
        # before await
        # worker_1 start
        # worker_1 done
        # awaited worker_1
        # worker_2 start
        # worker_2 done
        # awaited worker_2
        # TIME:  0:00:03.003704

    @staticmethod
    def the_asynchronous_process():
        import asyncio

        async def worker_1():
            print('worker_1 start')
            await asyncio.sleep(1)
            print('worker_1 done')

        async def worker_2():
            print('worker_2 start')
            await asyncio.sleep(2)
            print('worker_2 done')

        async def main():
            task1 = asyncio.ensure_future(worker_1())
            task2 = asyncio.ensure_future(worker_2())
            print('before await')
            await task1
            print('awaited worker_1')
            await task2
            print('awaited worker_2')

        from win32.timezone import now
        start = now()
        loop = asyncio.get_event_loop()
        task = loop.create_task(main())
        loop.run_until_complete(task)
        print('TIME: ', now() - start)

        ########## 输出 ##########
        # before await
        # worker_1 start
        # worker_2 start
        # worker_1 done
        # awaited worker_1
        # worker_2 done
        # awaited worker_2
        # TIME:  0:00:02.000649

    @staticmethod
    def limit_runtime_and_set_error_handling_for_coroutine_tasks():
        import asyncio

        async def worker_1():
            await asyncio.sleep(1)
            return 1

        async def worker_2():
            await asyncio.sleep(2)
            return 2 / 0

        async def worker_3():
            await asyncio.sleep(3)
            return 3

        async def main():
            task_1 = asyncio.ensure_future(worker_1())
            task_2 = asyncio.ensure_future(worker_2())
            task_3 = asyncio.ensure_future(worker_3())

            # 超过 2s 则取消任务三
            await asyncio.sleep(2)
            task_3.cancel()

            # 不设置 return_exceptions = True，错误会被抛出，需要使用 try except
            # 捕获，进而造成其他还没被执行的任务会被完全取消掉
            res = await asyncio.gather(task_1, task_2, task_3,
                                       return_exceptions=True)
            print(res)

        from win32.timezone import now
        start = now()
        loop = asyncio.get_event_loop()
        task = loop.create_task(main())
        loop.run_until_complete(task)
        print('TIME: ', now() - start)

    @staticmethod
    def customer_and_produce_model():
        import asyncio
        import random

        async def consumer(queue, id):
            while True:
                val = await queue.get()
                print('{} get a val: {}'.format(id, val))
                await asyncio.sleep(1)

        async def producer(queue, id):
            for i in range(5):
                val = random.randint(1, 10)
                await queue.put(val)
                print('{} put a val: {}'.format(id, val))
                await asyncio.sleep(1)

        async def main():
            queue = asyncio.Queue()

            consumer_1 = asyncio.ensure_future(consumer(queue, 'consumer_1'))
            consumer_2 = asyncio.ensure_future(consumer(queue, 'consumer_2'))

            producer_1 = asyncio.ensure_future(producer(queue, 'producer_1'))
            producer_2 = asyncio.ensure_future(producer(queue, 'producer_2'))

            await asyncio.sleep(10)
            consumer_1.cancel()
            consumer_2.cancel()

            await asyncio.gather(consumer_1, consumer_2, producer_1, producer_2,
                                 return_exceptions=True)

        from win32.timezone import now
        start = now()
        loop = asyncio.get_event_loop()
        task = loop.create_task(main())
        loop.run_until_complete(task)
        print('TIME: ', now() - start)

    @staticmethod
    def get_movies_from_douban_with_synchronous():
        import requests
        from bs4 import BeautifulSoup

        def main():
            url = "https://movie.douban.com/cinema/later/beijing/"
            init_page = requests.get(url).content
            init_soup = BeautifulSoup(init_page, 'lxml')

            all_movies = init_soup.find('div', id="showing-soon")
            for each_movie in all_movies.find_all('div', class_="item"):
                all_a_tag = each_movie.find_all('a')
                all_li_tag = each_movie.find_all('li')

                movie_name = all_a_tag[1].text
                url_to_fetch = all_a_tag[1]['href']
                movie_date = all_li_tag[0].text

                response_item = requests.get(url_to_fetch).content
                soup_item = BeautifulSoup(response_item, 'lxml')
                img_tag = soup_item.find('img')

                print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))

        main()

    @staticmethod
    def get_movies_from_douban_with_asynchronous():
        import asyncio
        import aiohttp

        from bs4 import BeautifulSoup

        header = header = {"User-Agent":
                             "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
                             " AppleWebKit/537.36 (KHTML, like Gecko)"
                             " Chrome/74.0.3729.157 Safari/537.36"}

        async def fetch_content(url):
            async with aiohttp.ClientSession(
                    headers=header, connector=aiohttp.TCPConnector(ssl=False)
            ) as session:
                async with session.get(url) as response:
                    return await response.text()

        async def main():
            url = "https://movie.douban.com/cinema/later/beijing/"
            init_page = await fetch_content(url)
            init_soup = BeautifulSoup(init_page, 'lxml')

            movie_names, urls_to_fetch, movie_dates = [], [], []

            all_movies = init_soup.find('div', id="showing-soon")
            for each_movie in all_movies.find_all('div', class_="item"):
                all_a_tag = each_movie.find_all('a')
                all_li_tag = each_movie.find_all('li')

                movie_names.append(all_a_tag[1].text)
                urls_to_fetch.append(all_a_tag[1]['href'])
                movie_dates.append(all_li_tag[0].text)

            tasks = [fetch_content(url) for url in urls_to_fetch]
            pages = await asyncio.gather(*tasks)

            for movie_name, movie_date, page in zip(movie_names, movie_dates,
                                                    pages):
                soup_item = BeautifulSoup(page, 'lxml')
                img_tag = soup_item.find('img')

                print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))

        from win32.timezone import now
        start = now()
        loop = asyncio.get_event_loop()
        task = loop.create_task(main())
        loop.run_until_complete(task)
        print('TIME: ', now() - start)

    @staticmethod
    def add_callback_function():
        import asyncio

        async def worker_1():
            print('worker_1 start')
            await asyncio.sleep(1)
            print('worker_1 done')

        async def worker_2():
            print('worker_2 start')
            await asyncio.sleep(2)
            print('worker_2 done')

        async def main():
            task1 = asyncio.ensure_future(worker_1())
            task2 = asyncio.ensure_future(worker_2())
            task1.add_done_callback(callback_function)
            task2.add_done_callback(callback_function)
            print('before await')
            await task1
            print('awaited worker_1')
            await task2
            print('awaited worker_2')

        def callback_function(future):
            print('invoked callback function')
            print('Callback: ', future.result())

        from win32.timezone import now
        start = now()
        loop = asyncio.get_event_loop()
        task = loop.create_task(main())
        loop.run_until_complete(task)
        print('TIME: ', now() - start)

        ########## 输出 ##########
        # before await
        # worker_1 start
        # worker_2 start
        # worker_1 done
        # awaited worker_1
        # worker_2 done
        # awaited worker_2
        # TIME:  0:00:02.000649


    @staticmethod
    def download_wiki():
        import asyncio
        import aiohttp
        import time

        async def download_one(url):
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    print('Read {} from {}'.format(resp.content_length, url))

        async def download_all(sites):
            tasks = [asyncio.ensure_future(download_one(site)) for site in sites]
            await asyncio.gather(*tasks)

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
            loop = asyncio.get_event_loop()
            task = loop.create_task(download_all(sites))
            loop.run_until_complete(task)
            end_time = time.perf_counter()
            print('Download {} sites in {} seconds'.format(
                len(sites), end_time - start_time))
        main()


class AsyncioStudyPython37(object):
    @staticmethod
    def synchronous_execution_python37():
        import asyncio
        # async 用于生命异步函数，调用异步函数，得到协程对象，这时并不会真正执行这个函数
        async def crawl_page(url):
            print('crawling {}'.format(url))
            sleep_time = int(url.split('_')[-1])
            await asyncio.sleep(sleep_time)
            print('OK {}'.format(url))

        async def main(urls):
            for url in urls:
                # await 用于执行函数，同步调用，程序会阻塞到这里，执行完毕后返回
                await crawl_page(url)

        # asyncio.run 来触发运行, 一个非常好的编程规范是，asyncio.run(main())
        # 作为程序的入口函数，在程序运行周期内，只调用一次 asyncio.run
        asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))

    @staticmethod
    def asynchronous_execution_python37():
        import asyncio

        async def crawl_page(url):
            print('crawling {}'.format(url))
            sleep_time = int(url.split('_')[-1])
            await asyncio.sleep(sleep_time)
            print('OK {}'.format(url))

        async def main(urls):
            # asyncio.create_task 来创建任务。任务创建后很快就会被调度执行，这样，我们的代码
            # 也不会阻塞在任务这里。所以，我们要等所有任务都结束才行
            tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
            # Method1:
            for task in tasks:
                await task
            # Method2:
            # *tasks 解包列表
            # await asyncio.gather(*tasks)
            asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))

    @staticmethod
    def limit_runtime_and_set_error_handling_for_coroutine_tasks():
        import asyncio

        async def worker_1():
            await asyncio.sleep(1)
            return 1

        async def worker_2():
            await asyncio.sleep(2)
            return 2 / 0

        async def worker_3():
            await asyncio.sleep(3)
            return 3

        async def main():
            task_1 = asyncio.create_task(worker_1())
            task_2 = asyncio.create_task(worker_2())
            task_3 = asyncio.create_task(worker_3())

            await asyncio.sleep(2)
            task_3.cancel()
            res = await asyncio.gather(task_1, task_2, task_3,
                                       return_exceptions=True)
            print(res)

        asyncio.run(main())

    @staticmethod
    def customer_and_produce_model():
        import asyncio
        import random

        async def consumer(queue, id):
            while True:
                val = await queue.get()
                print('{} get a val: {}'.format(id, val))
                await asyncio.sleep(1)

        async def producer(queue, id):
            for i in range(5):
                val = random.randint(1, 10)
                await queue.put(val)
                print('{} put a val: {}'.format(id, val))
                await asyncio.sleep(1)

        async def main():
            queue = asyncio.Queue()

            consumer_1 = asyncio.create_task(consumer(queue, 'consumer_1'))
            consumer_2 = asyncio.create_task(consumer(queue, 'consumer_2'))

            producer_1 = asyncio.create_task(producer(queue, 'producer_1'))
            producer_2 = asyncio.create_task(producer(queue, 'producer_2'))

            await asyncio.sleep(10)
            consumer_1.cancel()
            consumer_2.cancel()

            await asyncio.gather(consumer_1, consumer_2, producer_1, producer_2,
                                 return_exceptions=True)
        asyncio.run(main())

    @staticmethod
    def get_movies_from_douban_with_synchronous():
        import requests
        from bs4 import BeautifulSoup

        def main():
            url = "https://movie.douban.com/cinema/later/beijing/"
            init_page = requests.get(url).content
            init_soup = BeautifulSoup(init_page, 'lxml')

            all_movies = init_soup.find('div', id="showing-soon")
            for each_movie in all_movies.find_all('div', class_="item"):
                all_a_tag = each_movie.find_all('a')
                all_li_tag = each_movie.find_all('li')

                movie_name = all_a_tag[1].text
                url_to_fetch = all_a_tag[1]['href']
                movie_date = all_li_tag[0].text

                response_item = requests.get(url_to_fetch).content
                soup_item = BeautifulSoup(response_item, 'lxml')
                img_tag = soup_item.find('img')

                print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))
        main()

    @staticmethod
    def get_movies_from_douban_with_asynchronous():
        import asyncio
        import aiohttp

        from bs4 import BeautifulSoup

        async def fetch_content(url):
            async with aiohttp.ClientSession(
                    headers=header, connector=aiohttp.TCPConnector(ssl=False)
            ) as session:
                async with session.get(url) as response:
                    return await response.text()

        async def main():
            url = "https://movie.douban.com/cinema/later/beijing/"
            init_page = await fetch_content(url)
            init_soup = BeautifulSoup(init_page, 'lxml')

            movie_names, urls_to_fetch, movie_dates = [], [], []

            all_movies = init_soup.find('div', id="showing-soon")
            for each_movie in all_movies.find_all('div', class_="item"):
                all_a_tag = each_movie.find_all('a')
                all_li_tag = each_movie.find_all('li')

                movie_names.append(all_a_tag[1].text)
                urls_to_fetch.append(all_a_tag[1]['href'])
                movie_dates.append(all_li_tag[0].text)

            tasks = [fetch_content(url) for url in urls_to_fetch]
            pages = await asyncio.gather(*tasks)

            for movie_name, movie_date, page in zip(movie_names, movie_dates,
                                                    pages):
                soup_item = BeautifulSoup(page, 'lxml')
                img_tag = soup_item.find('img')

                print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))

        asyncio.run(main())

    @staticmethod
    def add_callback_function():
        import asyncio

        async def crawl_page(url):
            print('crawling {}'.format(url))
            sleep_time = int(url.split('_')[-1])
            await asyncio.sleep(sleep_time)
            print('OK {}'.format(url))

        async def main(urls):
            # asyncio.create_task 来创建任务。任务创建后很快就会被调度执行，这样，我们的代码
            # 也不会阻塞在任务这里。所以，我们要等所有任务都结束才行
            tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
            # Method1:
            for task in tasks:
                task.add_done_callback((lambda future:
                                        print('result: ', future.result())))
            await asyncio.gather(*tasks)
            asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))

    @staticmethod
    def download_wiki():
        import asyncio
        import aiohttp
        import time

        async def download_one(url):
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    print('Read {} from {}'.format(resp.content_length, url))

        async def download_all(sites):
            tasks = [asyncio.create_task(download_one(site)) for site in sites]
            await asyncio.gather(*tasks)

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
            asyncio.run(download_all(sites))
            end_time = time.perf_counter()
            print('Download {} sites in {} seconds'.format(
                len(sites), end_time - start_time))

        main()


if __name__ == '__main__':
    # AsyncioStudyPython37.synchronous_execution_python37()
    # AsyncioStudyPython37.asynchronous_execution_python37()

    # AsyncioStudyPython36.asynchronous_execution_python36()
    # AsyncioStudyPython36.synchronous_execution_python36()
    # AsyncioStudyPython36.the_synchronous_process()
    # AsyncioStudyPython36.the_asynchronous_process()
    # (AsyncioStudyPython36
    #     .limit_runtime_and_set_error_handling_for_coroutine_tasks())
    # AsyncioStudyPython36.customer_and_produce_model()
    # AsyncioStudyPython36.get_movies_from_douban_with_asynchronous()
    # AsyncioStudyPython36.add_callback_function()
    AsyncioStudyPython36.download_wiki()

