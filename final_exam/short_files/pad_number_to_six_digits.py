class PadNumberToSixDigits:
    def pad_number(self):
        display_width = 6
        raw_input = input("Enter a number (0-1000): ")
        print(f"Your number padded to {display_width} digits is: {raw_input.zfill(display_width)}")

if __name__ == "__main__":
    padder = PadNumberToSixDigits()
    padder.pad_number()
