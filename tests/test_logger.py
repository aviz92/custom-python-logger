import unittest
from custom_python_logger import get_logger


class TestLogger(unittest.TestCase):
    def test_logger_creation(self):
        logger = get_logger(project_name='TestProject')
        self.assertIsNotNone(logger)
        self.assertEqual(logger.name, 'root')

    def test_step_log(self):
        logger = get_logger(project_name='TestProject')
        logger.step('Testing step log')
        self.assertTrue(True)  # You can add more specific checks for actual logging output

    def test_exception_log(self):
        logger = get_logger(project_name='TestProject')
        try:
            raise ValueError("Test exception")
        except ValueError as e:
            logger.exception(f"Exception occurred: {e}")
        self.assertTrue(True)  # You can add more specific checks for actual logging output


if __name__ == '__main__':
    unittest.main()
