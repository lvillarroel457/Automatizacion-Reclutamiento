import os
import unittest

TEST_FILE_PATTERN = 'test*.py' 
ABSPATH = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    print(f'path: {ABSPATH}')
    test_suite = unittest.TestLoader().discover(start_dir=ABSPATH, pattern=TEST_FILE_PATTERN)
    unittest.TextTestRunner(verbosity=1).run(test_suite)
