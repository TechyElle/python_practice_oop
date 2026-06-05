class ManualRemovePrefix:
    def run(self):
        text_string = input("Enter string: ")
        prefix_string = input("Enter prefix: ")
        if text_string.startswith(prefix_string): print(f"Result is {text_string[len(prefix_string):]}")
        else: print(f"Result is {text_string}")

if __name__ == "__main__":
    ManualRemovePrefix().run()