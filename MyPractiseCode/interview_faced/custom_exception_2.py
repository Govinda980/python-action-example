class CustomException(Exception):
    def __init__(self, message="some thing went wrong"):
        super().__init__(message)


def risky_operation(num):
    if num < 0:
        raise CustomException("Number is Negative")
    else:
        return num * 2

try:
    ret_val = risky_operation(-10)
    print(ret_val)
except CustomException as e:
    print(e)
