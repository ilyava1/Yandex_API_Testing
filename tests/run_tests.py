from test_1_create_folder_on_disk import TestClass_1_Functions
from test_2_delete_folder_from_disk import TestClass_2_Functions

import unittest
from unittest import TestSuite


def load_tests(loader, tests, pattern):
    suite = TestSuite()
    for test_class in (TestClass_1_Functions, TestClass_2_Functions):
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite

unittest.main(verbosity=2)
