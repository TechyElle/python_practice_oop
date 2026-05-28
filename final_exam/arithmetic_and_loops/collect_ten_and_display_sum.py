class NumberSum:
    def __init__(self):
        self.total = 0

    def main(self):
        for i in range(10):
            num = float(input(f"Enter a number {i+1}: "))
            self.total += num

        print(f"Total: {self.total}")

if __name__ == "__main__":
    NumberSum().main()