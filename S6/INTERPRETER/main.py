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

class Substract(AbstractExpression):
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

    def __repr__(self):
        return f"({self.left} Substract {self.right})"


SENTENCE = "5 + 4 - 13 + 17 - 2"
print(SENTENCE)

TOKENS = SENTENCE.split(" ")
print(TOKENS)

AST:list[AbstractExpression] = []
AST.append(Add(Number(TOKENS[0]),Number(TOKENS[2]))) #5 + 4
AST.append(Substract(AST[0],Number(TOKENS[4]))) #^ - 13
AST.append(Add(AST[1],Number(TOKENS[6]))) #^ + 17
AST.append(Substract(AST[2],Number(TOKENS[8])))#^ -2

AST_ROOT = AST.pop()
print(AST_ROOT.interpret())
print(AST_ROOT)
