class ManualRJust:
    def run(self):
        # Get the text and how wide the final output should be
        text = input("Enter text: ")
        target_width = int(input("Enter total width: "))

        # Keep adding a space on the left until target_width is reached
        result = text
        while len(result) < target_width:
            result = " " + result

        # Display the right-justified result
        print(f"'{text}' right-justified to width {target_width} is: '{result}'")
        
if __name__ == "__main__":
    ManualRJust().run()