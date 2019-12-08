from unittest.mock import patch
import unittest

import main

class DailyScript(unittest.TestCase):

    def run_daily(self):
        user_input = [
            'login',
            'machine',
            'deposit',
            '1234567',
            '1000000',
        ]
        # expected_stacks = [
        #     [1, 2, 3, 2],
        #     [2],
        #     [],
        # ]
        with patch('builtins.input', side_effect=user_input):
            stacks = main.loop()
        self.assertEqual(stacks, expected_stacks)


if __name__ == '__main__':
    unittest.main()
