class ManualEndsWith:
    def main(self):
        text = input("Enter text: ")
        if text:
            suffix = input("Enter suffix to check: ")
            result = text.endswith(suffix)
            print(f"Does the text end with '{suffix}'? {result}")
        else:
            print("You did not enter any text.")

if __name__ == "__main__":
    ManualEndsWith().main()