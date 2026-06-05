class ManualRjust:
    def run(self):
        text_string = input("Enter string: ")
        total_length = int(input("Enter length: "))
        print(f"Result is {' ' * max(0, total_length - len(text_string)) + text_string}")

if __name__ == "__main__":
    ManualRjust().run()