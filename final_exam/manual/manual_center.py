class ManualCenter:
    def main(self):  
        text = input("Enter text: ")
        if text:
            width = len(text) + 4
            print(text.center(width))
        else:
            print("You did not enter any text.")

if __name__ == "__main__":
    ManualCenter().main()