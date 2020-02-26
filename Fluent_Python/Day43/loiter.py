print("\033c")

from time import sleep, strftime
from concurrent import futures


def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s...'

    display(msg.format('\t'*n, n, n))

    sleep(n)

    msg = '{}loiter({}): done.'

    display(msg.format('\t'*n, n))
    return n * 10


def main():
    display('\033[33mScript starting.\033[0m')

    executor = futures.ThreadPoolExecutor(max_workers=3)

    results = executor.map(loiter, range(5))

    display('\033[35mresults:\033[0m', results)

    display('\033[33mWaiting for individual results:\033[0m')

    breakpoint()
    for i, result in results:
        display('result {}: {}'.format(i, result))

    # for i, result in enumerate(results):
    #     display('result {}: {}'.format(i, result))


main()
