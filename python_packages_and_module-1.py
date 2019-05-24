# Question1: 输入日期， 判断这一天是这一年的第几天？
# Answer: 使用日期对象，然后做减法


def day_of_time():
    import datetime
    year = input("请输入年份: ")
    month = input("请输入月份: ")
    day = input("请输入天: ")
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    date2 = datetime.date(year=int(year), month=1, day=1)
    return (date1 - date2).days + 1

# Question2: 打乱排好序的 list 对象
# Answer： 使用 random 对象


def shuffle_list():
    import random
    a_list = [1, 2, 3, 4, 5]
    random.shuffle(a_list)
    print(a_list)


if __name__ == '__main__':
    print(day_of_time())

    #day_of_time()