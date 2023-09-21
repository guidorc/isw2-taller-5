#!./venv/bin/python
import unittest
from random import seed
from src.mutation_utils import insert_random_character, delete_random_character, change_random_character


class TestMutationUtils(unittest.TestCase):
    def testInsertionOnEmptyString(self):
        seed(1)
        s = ""
        mutant = insert_random_character(s)

        self.assertEqual(0, len(s))
        self.assertEqual(1, len(mutant))
        self.assertTrue(mutant.isprintable())
        self.assertEqual("h", mutant)

    def testInsertionOnString(self):
        seed(1)
        s = "Hello World"
        mutant = insert_random_character(s)

        self.assertEqual(len(s) + 1, len(mutant))
        self.assertTrue(mutant.isprintable())
        self.assertEqual("He+llo World", mutant)

    def testDeletionOnEmptyString(self):
        mutant = delete_random_character("")
        self.assertEqual("", mutant)

    def testDeletionOnString(self):
        seed(1)

        s = "Hello World"
        mutant = delete_random_character(s)

        self.assertEqual(len(s) - 1, len(mutant))
        self.assertTrue(mutant.isprintable())
        self.assertEqual("Helo World", mutant)

    def testChangeOnEmptyString(self):
        seed(1)
        mutant = change_random_character("")
        self.assertEqual("", mutant)

        s = "Hello World"
        mutant = change_random_character(s)

        self.assertEqual(len(s), len(mutant))
        self.assertTrue(mutant.isprintable())
        self.assertEqual("He+lo World", mutant)