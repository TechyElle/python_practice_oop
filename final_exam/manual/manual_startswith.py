class ManualStartsWith:
    def solve(self):
    # Get the text and the starting pattern to look for
        text = input("Enter the text: ")
        pattern = input("Enter the starting pattern: ") 
        # Check if the text starts with the given pattern
        if text.startswith(pattern):
            print(f"'{text}' starts with '{pattern}'")
        else:
            print(f"'{text}' does not start with '{pattern}'")
            
if __name__ == "__main__":
    solution = ManualStartsWith()
    solution.solve()