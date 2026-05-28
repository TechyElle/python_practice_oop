class ManualZfill:
    def run(self):
    # Get the text and how wide the zero-padded output should be
        text = input("Enter text: ")
        target_width = int(input("Enter total width: "))

        # Keep adding a zero on the left until target_width is reached
        while len(text) < target_width:
            text = "0" + text

        # Display the zero-padded result
        print(f"'{text}' zero-padded to width {target_width} is: '{text}'")

if __name__ == "__main__":
    solution = ManualZfill()
    solution.run()