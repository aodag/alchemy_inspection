import unittest
import doctest


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite([
        doctest.DocFileSuite('mapper.rst'),
        doctest.DocFileSuite('relation.rst'),
    ])
    return suite

if __name__ == '__main__':
    unittest.main()
