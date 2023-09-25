#!./venv/bin/python
import unittest
from random import seed
from src.crashme import crashme
from magic_fuzzer import MagicFuzzer


class TestEjercicio4(unittest.TestCase):

    def test_fuzzing_campaign_1(self):
        seed(122)
        fuzzer = MagicFuzzer([" "], crashme, function_name_to_call="crashme")
        lines_covered, iterations = fuzzer.run_until_covered(10000)
        self.assertEqual({2, 3, 4, 5, 6}, lines_covered)
        self.assertEqual(6834, iterations)

    def test_fuzzing_campaign_2(self):
        seed(74)
        fuzzer = MagicFuzzer([" "], crashme, function_name_to_call="crashme")
        lines_covered, iterations = fuzzer.run_until_covered(10000)
        self.assertEqual({2, 3, 4, 5, 6}, lines_covered)
        self.assertEqual(2450, iterations)

    def test_fuzzing_campaign_3(self):
        seed(63)
        fuzzer = MagicFuzzer([" "], crashme, function_name_to_call="crashme")
        lines_covered, iterations = fuzzer.run_until_covered(10000)
        self.assertEqual({2, 3, 4, 5, 6}, lines_covered)
        self.assertEqual(8292, iterations)

    def test_fuzzing_campaign_4(self):
        seed(147)
        fuzzer = MagicFuzzer([" "], crashme, function_name_to_call="crashme")
        lines_covered, iterations = fuzzer.run_until_covered(20000)
        self.assertEqual({2, 3, 4, 5, 6}, lines_covered)
        self.assertEqual(2032, iterations)

    def test_fuzzing_campaign_5(self):
        seed(155)
        fuzzer = MagicFuzzer([" "], crashme, function_name_to_call="crashme")
        lines_covered, iterations = fuzzer.run_until_covered(20000)
        self.assertEqual({2, 3, 4, 5, 6}, lines_covered)
        self.assertEqual(3467, iterations)