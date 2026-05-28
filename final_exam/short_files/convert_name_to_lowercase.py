class ConvertNameToLowercase:
    def solve(self):
        # Get the name from the user
        full_name = input("Enter your full name: ")

        # Make every letter small and display it
        print(f"Your name in lowercase is: {full_name.lower()}")

if __name__ == "__main__":
    solution = ConvertNameToLowercase()
    solution.solve()