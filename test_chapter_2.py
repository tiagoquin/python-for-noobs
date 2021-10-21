import chapter_2

def test_exercise2():
    assert chapter_2.exercise2('hello') == "HELLO"
    assert chapter_2.exercise2('HELLO') == "hello"
    assert chapter_2.exercise2('HeLlO') == "hElLo"

