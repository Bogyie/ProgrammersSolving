from datetime import datetime
from functools import wraps

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f'Success. {end-start} taken for {func.__name__}')
        return result
    return wrapper