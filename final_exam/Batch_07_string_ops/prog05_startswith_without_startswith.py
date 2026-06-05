class ManualStartswith:
    def run(self):
        text_string = input("Enter string: ")
        prefix_string = input("Enter prefix: ")
        print(f"Result is {text_string[:len(prefix_string)] == prefix_string}")

if __name__ == "__main__":
    ManualStartswith().run()