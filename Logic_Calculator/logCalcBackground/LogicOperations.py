import abc
from ast import Str

class Variable:
    def __init__(self, name:Str, value:bool = False) -> None:
        self.Name = name
        self.Value = False
    
    def setValue(self, value:bool):
        self.Value = value

    def getValue(self) -> bool:
        return self.Value

class LogicalOperator(abc.ABC):
    def __init__(self) -> None:
        pass
    
    @abc.abstractmethod
    def __str__(self) -> str:
        pass

    @abc.abstractmethod
    def calculateValue(self):
        pass

class Identity(LogicalOperator):
    def __init__(self, variable:Variable) -> None:
        super().__init__()
        self.Variable = variable

    def calculateValue(self):
        return self.Variable.getValue()
    
    def __str__(self) -> str:
        return self.Variable.Name

class Implication(LogicalOperator):
    def __init__(self, leftPart:LogicalOperator, rightPart:LogicalOperator) -> None:
        super().__init__()
        self.leftPart = leftPart
        self.rightPart = rightPart
    
    def calculateValue(self) -> bool:
        if(self.leftPart.calculateValue() and not self.rightPart.calculateValue()): return False
        return True
    
    def __str__(self) -> str:
        return f"({self.leftPart} -> {self.rightPart})"

class And(LogicalOperator):
    def __init__(self, leftPart:LogicalOperator, rightPart:LogicalOperator) -> None:
        super().__init__()
        self.leftPart = leftPart
        self.rightPart = rightPart
    
    def calculateValue(self) -> bool:
        return self.leftPart.calculateValue() and self.rightPart.calculateValue()
    
    def __str__(self) -> str:
        return f"{self.leftPart} ^ {self.rightPart}"

class Or(LogicalOperator):
    def __init__(self, leftPart:LogicalOperator, rightPart:LogicalOperator) -> None:
        super().__init__()
        self.leftPart = leftPart
        self.rightPart = rightPart

    def calculateValue(self) -> bool:
        return self.leftPart.calculateValue() or self.rightPart.calculateValue()
    
    def __str__(self) -> str:
        return f"{self.leftPart} v {self.rightPart}"

class Equivalence(LogicalOperator):
    def __init__(self, leftPart:LogicalOperator, rightPart:LogicalOperator) -> None:
        super().__init__()
        self.leftPart = leftPart
        self.rightPart = rightPart
    
    def calculateValue(self):
        return self.calculateValue() == self.calculateValue()
    
    def __str__(self) -> str:
        return f"{self.leftPart} <-> {self.rightPart}"

class Not(LogicalOperator):
    def __init__(self, identity: LogicalOperator) -> None:
        super().__init__()
        self.identity = identity
    
    def calculateValue(self) -> bool:
        return not self.identity.calculateValue()
    
    def __str__(self) -> str:
        return f"-{self.identity}"

if __name__ == '__main__':
    # Test Ausdruck: -a v (b -> c ^ -a)

    a = Variable("a")
    b = Variable("b")
    c = Variable("c")

    term = Or(
        Not(Identity(a)),
        Implication(
            Identity(b),
            And(
                Identity(c),
                Not(Identity(a))
            )
        )
    )

    print(term)