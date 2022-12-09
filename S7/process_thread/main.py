from time import sleep
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from after5 import return_after_5s


def main():
    pool = ProcessPoolExecutor(3)
    future = pool.submit(return_after_5s,("to jest istotny komunikat nr 55"))
    print(future.done())
    sleep(5)
    print(future.done())
    print(future.result())
    print(future.done())

if __name__ == '__main__':
    main()
