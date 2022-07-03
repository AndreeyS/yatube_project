import time

global_variable = 'Глобальная'


def some_func(passed_variable):
    local_variable = 'Локальная'

    def inside_func():
        inside_local_var = 'Внутренняя'
        return(f'{global_variable} '
               f'{local_variable} '
               f'{passed_variable} '
               f'{inside_local_var}')

    return inside_func


magic = some_func('Параметр')
print(magic())
another_magic = some_func('Другой параметр')
print(another_magic())


def some_func2(passed_arg):
    def inner_func(inner_passed_arg):
        return f'{passed_arg}, {inner_passed_arg}'

    return inner_func


hello_decor = some_func2('Hello')
bye_decor = some_func2('Goodbye')

print(hello_decor('Andreey'), '...', bye_decor('Andreey'), sep='\n')


def spech(text, volume):

    def whisper():
        return f'{text.lower()}...'

    def scream():
        return f'{text.upper()}!!!!!!11'

    return scream if volume > 50 else whisper


scream = spech('Duuude, Clouser is siiiimple', 60)
print(scream())
whisp = spech('Duuude, Clouser is siiimple', 40)
print(whisp())

print()
print()


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = round(time.time() - start_time, 100)
        print(f'{execution_time} of {func.__name__}')
        return result
    return wrapper


def funk2(x):
    return x*x


test_dec = time_decorator(funk2)
print(test_dec(4))


def uppercase_decorator(func):
    def wrapper(word):
        original_result = func(word)
        return original_result.upper()
    return wrapper

@uppercase_decorator
def lowercase(word):
    a = 1
    return f'{word.lower()}'


upper = uppercase_decorator(lowercase)

lowercase(('HelLo'))

print([i for i in dir(lowercase)], sep='\n')
print(lowercase.__dict__)


