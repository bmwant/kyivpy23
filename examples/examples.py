import sys
import time
import contextvars


def pep562():
    from examples.my_module import old_function

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


var = contextvars.ContextVar('var')
var.set('spam')

def pep567():
    # 'var' was set to 'spam' before
    # calling 'copy_context()' and 'ctx.run(main)', so:
    # var.get() == ctx[var] == 'spam'

    var.set('ham')

    # Now, after setting 'var' to 'ham':
    # var.get() == ctx[var] == 'ham'

ctx = contextvars.copy_context()

# Any changes that the 'main' function makes to 'var'
# will be contained in 'ctx'.
ctx.run(pep567)

print(ctx.get(var))  # ham
print(var.get())  # spam


if __name__ == '__main__':
    sys.breakpointhook = lambda: print('Do not touch anything')
    # pep562()
    # pep553()
    # pep564()
    pep567()
