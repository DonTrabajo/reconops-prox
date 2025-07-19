def tool(*args, **kwargs):
    def decorator(func):
        return func
    return decorator
