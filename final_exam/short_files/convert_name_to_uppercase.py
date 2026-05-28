class ConvertNameToUppercase:
    def solve(self):
        name = input("Enter your name: ")
        uppercase_name = name.upper()
        print("Your name in uppercase is:", uppercase_name)

if __name__ == "__main__":
    converter = ConvertNameToUppercase()
    converter.solve()
