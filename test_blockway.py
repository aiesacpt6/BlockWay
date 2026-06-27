# test_blockway.py
"""
Tests for BlockWay module.
"""

import unittest
from blockway import BlockWay

class TestBlockWay(unittest.TestCase):
    """Test cases for BlockWay class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockWay()
        self.assertIsInstance(instance, BlockWay)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockWay()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
