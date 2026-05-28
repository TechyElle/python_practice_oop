class ConvertNameToSnakeCase:
    def solve(self):
        # Get the name from the user
        full_name = input("Enter your full name: ")
        # Convert the name to snake_case and display it
        snake_case_name = '_'.join(word.lower() for word in full_name.split())
        print(f"Your name in snake_case is: {snake_case_name}") 

if __name__ == "__main__":
    solution = ConvertNameToSnakeCase()
    solution.solve()