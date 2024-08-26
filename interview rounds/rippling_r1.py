class Cell:
    def __init__(self,value=""):
        self.value=value

class Excel:
    def __init__(self):
        self.cells={}

    def get(self,cell_id):
        return self.cells[cell_id] if cell_id in self.cells else ""

    def set(self,cell_id,value):
        self.cells[cell_id]=Cell(value)

class EvaluateExpression:
    def __init__(self,excel):
        self.excel=excel

    def evaluate(self):
        cells=self.excel.cells

        for cell_id in cells:
            expression=cells[cell_id]
            if expression[0]=="=":
                token=self.tokenize(expression)
                ans=self.evaluate_token(token)
                print(f'{cell_id}= {expression} {ans}')
            else:
                print(f'{cell_id}= {expression} {expression}')

    def tokenize(self,expression):
        tokens=[]
        i=0
        n=len(expression)
        while i<n:
            if expression[i].isdigit() or (expression[i]=='-' and (i+1<n and expression[i+1].isdigit())):
                start=i
                if expression[i]=="-":
                    i+=1
                while i<n and expression[i].isdigit():
                    i+=1
                tokens.append(expression[start:i])
            elif expression[i].isalpha():
                start=i
                while i<n and expression[i].isalpha():
                    i+=1
                while i<n and expression[i].isdigit():
                    i+=1


    def evaluate_token(self,token):

