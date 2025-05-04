from lesson_18.homework_18 import ReverseList, exception_decorator


class TestHomework18:

    @exception_decorator("Expected a list, got <class 'int'>")
    def test_catch_exception(self):
        ReverseList(1)
