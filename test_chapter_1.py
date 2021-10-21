import chapter_1


import unittest


class TestExercise1(unittest.TestCase):
    def test_exercise1(self):
        assert type(chapter_1.exercise1()) == int

    def test_exercise2(self):
        assert type(chapter_1.exercise2()) == float

    def test_exercise3(self):
        assert type(chapter_1.exercise3()) == bool

    def test_exercise4(self):
        assert type(chapter_1.exercise4()) == str

    def test_exercise5(self):
        assert chapter_1.exercise5() == 5

    def test_exercise6(self):
        assert chapter_1.exercise6(1) == 0
        assert chapter_1.exercise6(42) == 0
        assert chapter_1.exercise6(99) == 0

    def test_exercise7(self):
        assert chapter_1.exercise7(1) % 2 == 0
        assert chapter_1.exercise7(42) % 2 == 0
        assert chapter_1.exercise7(99) % 2 == 0


if __name__ == "__main__":
    unittest.main()
