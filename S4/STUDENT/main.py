from homework import  HomeWork
from exam import Exam

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

