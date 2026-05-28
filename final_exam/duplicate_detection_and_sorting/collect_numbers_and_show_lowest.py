class ShowLowest:
    def main(self):
        numbers = []
        while True:
            try:
                num = float(input("Enter a number (or 'q' to quit): "))
                numbers.append(num)
            except ValueError:
                break
        if numbers:
            lowest = min(numbers)
            print(f"The lowest number entered is: {lowest}")
        else:
            print("No numbers were entered.")

if __name__ == "__main__":
    ShowLowest().main()