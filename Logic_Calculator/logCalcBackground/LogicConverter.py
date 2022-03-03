from LogicOperations import *

# -(a v b)
# -a v b

def convertTerm(term:str) -> LogicalOperator:
    term = term.replace(" ","")
    if len(term) == 0: return None
    lexerArr = []
    
        


    
if __name__ == '__main__':
    print(convertTerm("-a v -b"))
    