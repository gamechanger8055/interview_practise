import re
class Cell:
    def __init__(self,value='0'):
        self.value=value

class Excel:
    def __init__(self):
        self.cells={}

    def set(self,cell_name,value):
        self.cells[cell_name]=Cell(value)

    def get(self,cell_name):
        return self.cells[cell_name].value if cell_name in self.cells else '0'

class ExpressionEvaluator:
    def __init__(self,excel):
        self.excel=excel

    def evaluate(self,expression):
        tokens=self.tokenize(expression)
        #print(tokens)
        return self.evaluate_tokens(tokens)

    def tokenize(self,expression):
        return re.findall(r'[A-Z]+[0-9]+|\d+|[-+]',expression)

    def evaluate_tokens(self,tokens):
        stack=[]
        current_operator='+'
        print(tokens)
        for token in tokens:
            print("hhg",stack,token)
            if token.isdigit() or (token[1:].isdigit() and token[0]=="-"):
                if current_operator=="+":
                    stack.append(int(token))
                elif current_operator=="-":
                    stack.append(-int(token))
            elif re.match(r'[A-Z]+[0-9]+', token):
                value = self.evaluate(self.excel.get(token))
                if current_operator == '+':
                    stack.append(value)
                elif current_operator == '-':
                    stack.append(-value)
                else:
                    current_operator = token
        return sum(stack)


excel = Excel()
evaluator = ExpressionEvaluator(excel)

# Example usage
excel.set('A1', '5')
excel.set('B2', 'A1+3')
print(evaluator.evaluate(excel.get('B2')))  # Output should be 8