class ManualIsupper:
    def run(self):
        user_input = input("Enter string: ")
        output = all(char.upper() == char and not char.islower() for char in user_input if char.isalpha())
        print(f"Result is {output}")

if __name__ == "__main__":
    ManualIsupper().run()
    