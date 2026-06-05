class ManualRstrip:
    def run(self):
        text_string = input("Enter string: ")
        index = len(text_string) - 1
        while index >= 0 and text_string[index] == ' ': index -= 1
        print(f"Result is {text_string[:index + 1]}")

if __name__ == "__main__":
    ManualRstrip().run()