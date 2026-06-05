class ManualRemoveSuffix:
    def run(self):
        text_string = input("Enter string: ")
        suffix_string = input("Enter suffix: ")
        if text_string.endswith(suffix_string): 
            print(f"Result is {text_string[:-len(suffix_string)]}")
        else: 
            print(f"Result is {text_string}")

if __name__ == "__main__":
    ManualRemoveSuffix().run()