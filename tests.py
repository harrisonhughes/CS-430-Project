import unittest

import algorithmEngine
import blockNestedLoops
import nestedLoop


class MyTestCase(unittest.TestCase):
    def test_blocked_nested_loop(self):
        dataset = algorithmEngine.createTestData(100)
        self.assertEqual(nestedLoop.nestedLoop(dataset), blockNestedLoops.block_nested_loop(dataset))


if __name__ == '__main__':
    unittest.main()
