from warnings import warn

deprecated_names = ['old_function']


def old_function():
    return 5.1


def __getattr__(name):
    if name in deprecated_names:
        warn(f'{name} is deprecated', DeprecationWarning)
        return globals()[name]
    raise AttributeError(f'module {__name__} has no attribute {name}')
