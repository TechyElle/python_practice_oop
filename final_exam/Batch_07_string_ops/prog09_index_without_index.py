class ManualIndex:
    def run(self):
        text_string = input("Enter string: ")
        substring = input("Enter substring: ")
        print(f"Result is {text_string.find(substring)}")

if __name__ == "__main__":
    ManualIndex().run()