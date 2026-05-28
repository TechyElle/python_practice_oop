class ConvertNameToPascalCase:
    def solve(self):
        # Get the name from the user
        full_name = input("Enter your full name: ")

        # Convert the name to PascalCase and display it
        pascal_case_name = ''.join(word.capitalize() for word in full_name.split())
        print(f"Your name in PascalCase is: {pascal_case_name}")
        
if __name__ == "__main__":
    solution = ConvertNameToPascalCase()
    solution.solve()

