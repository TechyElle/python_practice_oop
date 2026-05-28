class ShowHighest:
    def main(self):
        numbers = []
        while True:
            try:
                num = float(input("Enter a number (or 'q' to quit): "))
                numbers.append(num)
            except ValueError:
                break
        if numbers:
            highest = max(numbers)
            print(f"The highest number entered is: {highest}")
        else:
            print("No numbers were entered.")

if __name__ == "__main__":
    ShowHighest().main()