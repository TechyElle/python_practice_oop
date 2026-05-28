class Subtracter:
    def __init__(self):
        self.first_num = 0
        self.second_num = 0

    def main(self):
        # read inputs
        self.first_num = float(input("Enter first: "))
        self.second_num = float(input("Enter second: "))

        # subtract and display
        total = self.first_num - self.second_num
        print(f"Difference is {total}")

if __name__ == "__main__":
    Subtracter().main()