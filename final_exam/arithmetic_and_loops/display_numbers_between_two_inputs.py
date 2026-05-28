class NumbersBetween:
    def __init__(self):
        self.start = 0
        self.end = 0

    def main(self):
        self.start = int(input("Enter the first number: "))
        self.end = int(input("Enter the second number: "))

        print(f"Numbers between {self.start} and {self.end}:")
        for num in range(self.start + 1, self.end):
            print(num)

if __name__ == "__main__":
    numbers_between = NumbersBetween()
    numbers_between.main()