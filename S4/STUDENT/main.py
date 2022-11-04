from homework import  HomeWork
from exam import Exam

import grade as g



gal = HomeWork()
gal.grade = 93
assert gal.grade == 93
print(f"ocena za projekt: {gal.grade}")

print("________ Exam class ___________")

ex = Exam()
ex.writing_grade = 83
ex.math_grade = 99

assert ex.writing_grade == 83
assert ex.math_grade == 99

print(ex.writing_grade)
print(ex.math_grade)


print("__________ klasa Gade, Exam ____________________")

exam = g.Exam()
exam.writing_grade = 40

g.Exam.__dict__['writing_grade'].__set__(exam,40)

#exam.writing_grade

p = g.Exam.__dict__['writing_grade'].__get__(exam,g.Exam)

print(p)

print("__________ zmodyfikowana klasa Gade, Exam ____________________")

firstexam = g.Exam()
firstexam.writing_grade = 81
firstexam.science_grade = 65

print(f'Pisanie - ocena {firstexam.writing_grade}')
print(f'Nauka - ocena {firstexam.science_grade}')
