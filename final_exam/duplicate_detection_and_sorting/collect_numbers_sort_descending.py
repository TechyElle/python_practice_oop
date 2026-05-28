class DescendingSort:
    def main(self):
        numbers = []
        while True:
            try:
                num = float(input("Enter a number (or 'q' to quit): "))
                numbers.append(num)
            except ValueError:
                break
        numbers.sort(reverse=True)
        print("Numbers in descending order:")
        for num in numbers:
            print(num)

if __name__ == "__main__":
    DescendingSort().main()