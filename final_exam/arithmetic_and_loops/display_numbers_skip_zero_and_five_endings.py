class SkipZeroAndFiveEndings:
    def __init__(self):
        self.start = 0
        self.end = 100

    def main(self):
        for num in range(self.start, self.end + 1):
            # Check if the last digit is 0 or 5
            last_digit = num % 10
            # If the last digit is not 0 and not 5, display the number          
            if last_digit != 0 and last_digit != 5:
                print(f"Number: {num}")

if __name__ == "__main__":
    SkipZeroAndFiveEndings().main()
