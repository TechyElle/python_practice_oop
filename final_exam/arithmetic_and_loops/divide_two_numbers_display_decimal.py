class Divider:
    def __init__(self):
        self.num_one = 0
        self.num_two = 0

    def main(self):
        # input numbers
        self.num_one = float(input("First: "))
        self.num_two = float(input("Second: "))

        # show decimal result
        print(f"Result: {self.num_one / self.num_two}")

if __name__ == "__main__":
    Divider().main()
