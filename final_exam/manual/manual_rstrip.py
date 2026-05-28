class ManualRStrip:
    def solve(self):
        # Get the text which may have trailing spaces
        text = input("Enter text: ")

        # Walk backwards from the end until a real character appears
        end_index = len(text) - 1
        while end_index >= 0 and text[end_index] == " ":
            end_index -= 1

        # Display everything up to and including that last real character
        print(f"'{text}' with trailing spaces removed is: '{text[:end_index + 1]}'")

if __name__ == "__main__":
    ManualRStrip().solve()
