import unittest
from concurrent.futures import ThreadPoolExecutor


class TestExample(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)

    def test_case_2(self):
        self.assertEqual(2 * 2, 4)

    def test_case_3(self):
        self.assertEqual(3 - 1, 2)


def run_test_in_parallel(test_suite):
    def run_test_case(test_case):
        result = unittest.TextTestResult(stream=None, descriptions=False, verbosity=2)
        test_case.run(result)
        return result

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(run_test_case, test) for test in test_suite]
        results = [future.result() for future in futures]
    return results


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestExample)
    run_test_in_parallel(suite)
