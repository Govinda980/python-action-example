class CustomException(Exception):
    pass


def check_positive(number):
    if number < 0:
        raise CustomException("Not positive number")


try:
    check_positive(-9)
except CustomException as e:
    print(e)










