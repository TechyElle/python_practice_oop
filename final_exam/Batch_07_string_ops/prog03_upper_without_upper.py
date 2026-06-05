class ManualUpper:
    def run(self):
        user_input = input("Enter string: ")
        output = "".join(chr(ord(char) - 32) if 'a' <= char <= 'z' else char for char in user_input)
        print(f"Result is {output}")

if __name__ == "__main__":
    ManualUpper().run()