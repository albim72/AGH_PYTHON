class HomeWork:

    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,value):
        if (0<=value<=100):
            raise ValueError('ocena musi być z zakresu od 0 do 100')
        self._grade = value
