class IsLower:
    def main(self):
        text = input("Enter text: ")
        if text:
            result = text.islower()
            print(f"Is the text in lowercase? {result}")
        else:
            print("You did not enter any text.")

if __name__ == "__main__":
    IsLower().main()