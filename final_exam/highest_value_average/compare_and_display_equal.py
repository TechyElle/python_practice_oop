class EqualityChecker:
    """A class to check if two numbers are equal and display the result."""
    def __init__(self):
        self.first_num = 0.0
        self.second_num = 0.0
        
    def main(self):
        # ask inputs
        self.first_num = float(input("Enter first number: "))
        self.second_num = float(input("Enter second number: "))
        # check for equality
        if self.first_num == self.second_num:
            print("Equal")
        else:
            print("Not equal")

if __name__ == "__main__":
    EqualityChecker().main()
