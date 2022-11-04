class Grade:

    def __init__(self):
        self._value = 0

    def __get__(self, instance, instance_type):
        return self._value

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('ocena musi być z zakresu od 0 do 100')
        self._grade = value


class Exam:

    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()
