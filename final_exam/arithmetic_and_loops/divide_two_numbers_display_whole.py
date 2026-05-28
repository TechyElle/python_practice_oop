class Divide:
    """Accept two numbers and display the quotient as a whole number."""
    def __init__(self):
        self.first_num = 0
        self.second_num = 0

    def main(self):
        # Get two numbers
        self.first_num = int(input("Enter first number: "))
        self.second_num = int(input("Enter second number: "))
        # Show the quotient       
        print(f"Quotient is {self.first_num // self.second_num}")   

if __name__ == "__main__":
    Divide().main()
