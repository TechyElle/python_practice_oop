class ManualSwapCase:
    def run(self):
        # Get the text from the user
        text = input("Enter text: ")
        # Flip each letter using its ASCII offset, leave other characters alone
        result = ""
        for char in text:
            if "A" <= char <= "Z":
                result += chr(ord(char) + 32)
            elif "a" <= char <= "z":
                result += chr(ord(char) - 32)
            else:
                result += char
        # Display the result with case swapped
        print(f"'{text}' with case swapped is: '{result}'")
        
if __name__ == "__main__":
    ManualSwapCase().run()