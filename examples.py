import sys
import time


def pep562():
    from my_module import old_function

    print(old_function())


def my_breakpoint():
    print('Nothing to do here')


def pep553():
    breakpoint()
    return 553


def pep564():
    print(time.clock_gettime_ns(0))
    print(time.monotonic_ns())
    print(time.perf_counter_ns())
    print(time.process_time_ns())
    print(time.time_ns())


if __name__ == '__main__':
    sys.breakpointhook = lambda: print('Do not touch anything')
    pep562()
    pep553()
    # pep564()
