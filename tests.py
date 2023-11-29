import unittest

import algorithmEngine
import blockNestedLoops


class MyTestCase(unittest.TestCase):
    def test_blocked_nested_loop(self):
        dataset = algorithmEngine.createTestData(100)
        self.assertEqual(algorithmEngine.nestedLoop(dataset), blockNestedLoops.block_nested_loop(dataset))


if __name__ == '__main__':
    unittest.main()
