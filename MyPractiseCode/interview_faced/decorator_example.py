def convert_to_lower(func):
    def wrapper(arg1, arg2):
        arg1 = arg1.lower()
        arg2 = arg2.lower()
        return func(arg1, arg2)

    return wrapper


def convert_to_upper(func):
    def wrapper():
        text = func().upper()
        return text

    return wrapper


@convert_to_upper
def test():
    return "Hello Words"


@convert_to_lower
def say_hello(name, sur_name):
    return f"My name is {name} and Sur name  is {sur_name}"


if __name__ == '__main__':
    print(say_hello('Govinda', 'Gupta'))
    print(test())
