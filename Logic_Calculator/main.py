
# Converts the String Input of an Variable to an useable Input 
from ast import In
from tkinter import SW, wantobjects


def parse_input(userInput:str):
    pass

# Converts the String Input of an Logical equation to an useable input
def parse_logic(equation:str):
    pass


if __name__ == "__main__":
    # Implement Regex to check if equation is valid
    equation = input("Logical equation: ")
    
    wantsQuit = False
    while not wantsQuit:
        userInput = input("(E)xport to CSV (T)est Input (S)how Table (Q)uit - ")

        # Functions: 
        # Export to csv
        # Test Input
        # Show Table
        # Quit

        if userInput == "Q" or userInput == "q":
            wantsQuit = True
        elif userInput == "E" or userInput == "e":
            pass
        elif userInput == "T" or userInput == "t":
            pass
        elif userInput == "S" or userInput == "s":
            pass
        



    

