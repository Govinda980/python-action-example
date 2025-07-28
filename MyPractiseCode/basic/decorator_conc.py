def convert_to_lower_case(function):
    def wrapper(arg1, arg2):
        arg1 = arg1.lower()
        arg2 = arg2.lower()
        convert_lower = function(arg1, arg2)
        return convert_lower

    return wrapper


@convert_to_lower_case
def say(name, address):
    return f"my name is {name} and i am from {address}"


print(say("Riyansh", "Dharahari"))


# decorator function to convert to lowercase
def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        return string_lowercase

    return wrapper


# decorator function to split words
def splitter_decorator(function):
    def wrapper():
        func = function()
        string_split = func.split()
        return string_split

    return wrapper


@splitter_decorator  # this is executed next
@lowercase_decorator  # this is executed first
def hello():
    return 'Hello World'


hello()  # output => [ 'hello' , 'world' ]
