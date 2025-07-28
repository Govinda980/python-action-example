import unittest

class TestMath(unittest.TestCase):
	def test_add(self):
		self.assertEqual(1 + 1, 2)

class TestString(unittest.TestCase):
	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

def suite():
	suite = unittest.TestSuite()
	suite.addTest(TestMath('test_add'))
	suite.addTest(TestString('test_upper'))
	return suite

if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	runner.run(suite())