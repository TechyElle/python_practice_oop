class ManualCapitalize:
    def main(self):
        text = input("Enter text: ")
        if text:
            result = text[0].upper() + text[1:].lower()
            print(f"Result is: {result}")
        else:
            print("You did not enter any text.")

if __name__ == "__main__":
    ManualCapitalize().main()