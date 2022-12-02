#Koncepcja wzorca Interpreter

class AbstractExpression:
    @staticmethod
    def interpret():
        """
        ta metoda będzie wywołana rekurencyjnie dla każdego AbstractExpression
        :return: 
        """
class Number(AbstractExpression):
    def __init__(self,value):
        self.value = int(value)
        
    def interpret(self):
        return self.value
    
    def __repr__(self):
        return str(self.value)
    
class Add(AbstractExpression):
    def __init__(self,left,right):
        self.left = left
        self.right = right
        
    def interpret(self):
        return self.left.interpret() + self.right.interpret()
    
    def __repr__(self):
        return f"({self.left} Add {self.right})"
    
