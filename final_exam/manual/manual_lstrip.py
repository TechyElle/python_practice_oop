class ManualLstrip:
    def solve(self):
        # Get the text which may have leading spaces
        text = input("Enter text: ")
        # Remove leading spaces manually
        result = ""
        leading_space = True
        for char in text:
            if char != ' ':
                leading_space = False
            if not leading_space:
                result += char
        # Print the result without leading spaces
        print("Text without leading spaces:", result)

if __name__ == "__main__":
    solution = ManualLstrip()
    solution.solve()