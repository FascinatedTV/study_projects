from LogicConverter import convertTerm
from LogicOperations import LogicalOperator

def generateTable(term:str):
    convertedTerm = convertTerm(term)
    variables = getVariables(term)
    


