import os
import unittest


def write_to_file(file_name, content):
    with open(file_name, 'w') as f1:
        f1.write(content)


class TestFileOperation(unittest.TestCase):

    def setUp(self):
        self.file_name = 'test_file.txt'
        with open(self.file_name, 'w') as f1:
            f1.write("Initial Content")

    def tearDown(self):
        try:
            os.remove(self.file_name)
        except FileNotFoundError as e:
            print(e)

    def test_write_to_file(self):
        new_content = "Hi Riyansh"
        write_to_file(self.file_name, new_content)
        with open(self.file_name, 'r') as f1:
            content = f1.read()
        self.assertEqual(new_content, content)

    def test_write_to_file_empty(self):
        write_to_file(self.file_name, '')
        with open(self.file_name, 'r') as f1:
            content = f1.read()
        self.assertEqual(content, '')


if __name__ == '__main__':
    unittest.main(verbosity=2)
