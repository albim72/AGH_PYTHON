class Grade:
    
    def __get__(self, instance, instance_type):
        pass
    
    def __set__(self, instance, value):
        pass
    

class Exam:
    
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()
