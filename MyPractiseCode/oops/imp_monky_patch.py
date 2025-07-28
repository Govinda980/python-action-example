import mock


def fun_to_replace(self):
    print("i am replacing function in mock")


mock.A.fun_in_mock = fun_to_replace
ob = mock.A()
ob.fun_in_mock()
