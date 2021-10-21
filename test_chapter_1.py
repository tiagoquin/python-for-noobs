import chapter_1


def test_exercise1():
    assert type(chapter_1.exercise1()) == int


def test_exercise2():
    assert type(chapter_1.exercise2()) == float


def test_exercise3():
    assert type(chapter_1.exercise3()) == bool


def test_exercise4():
    assert type(chapter_1.exercise4()) == str


def test_exercise5():
    assert chapter_1.exercise5() == 5


def test_exercise6():
    assert chapter_1.exercise6(1) == 0
    assert chapter_1.exercise6(42) == 0
    assert chapter_1.exercise6(99) == 0


def test_exercise7():
    assert chapter_1.exercise7(1) % 2 == 0
    assert chapter_1.exercise7(42) % 2 == 0
    assert chapter_1.exercise7(99) % 2 == 0


if __name__ == "__main__":
    test_exercise1()
    test_exercise2()
    test_exercise3()
    test_exercise4()
    test_exercise5()
    test_exercise6()
    test_exercise7()
