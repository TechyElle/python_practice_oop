class ManualEndswith:
    def run(self):
        text_string = input("Enter string: ")
        suffix_string = input("Enter suffix: ")
        print(f"Result is {text_string[-len(suffix_string):] == suffix_string if suffix_string else True}")

if __name__ == "__main__":
    ManualEndswith().run()