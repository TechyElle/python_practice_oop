class ManualLower:
    def run(self):
        user_input = input("Enter string: ")
        output = "".join(chr(ord(char) + 32) if 'A' <= char <= 'Z' else char for char in user_input)
        print(f"Result is {output}")

if __name__ == "__main__":
    ManualLower().run()