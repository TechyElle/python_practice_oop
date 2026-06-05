class ManualSwapcase:
    def run(self):
        user_input = input("Enter string: ")
        output = "".join(char.lower() if char.isupper() else char.upper() for char in user_input)
        print(f"Result is {output}")

if __name__ == "__main__":
    ManualSwapcase().run()