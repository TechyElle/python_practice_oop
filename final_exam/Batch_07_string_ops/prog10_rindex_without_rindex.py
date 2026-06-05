class ManualRindex:
    def run(self):
        text_string = input("Enter string: ")
        substring = input("Enter substring: ")
        print(f"Result is {text_string.rfind(substring)}")

if __name__ == "__main__":
    ManualRindex().run()