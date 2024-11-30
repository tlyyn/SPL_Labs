import unittest
import os
import sys

def run():
    # Add the project root to sys.path to ensure imports work correctly
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Load and run tests from test_calculator.py
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=os.path.dirname(__file__), pattern="test_calculator.py")
    runner = unittest.TextTestRunner(verbosity=2)  # Set verbosity to 2 for detailed output
    runner.run(suite)
