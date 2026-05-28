class NumberSkipper:
    def __init__(self):
        self.limit = 100

    def main(self):
        # loop to limit
        for num in range(self.limit + 1):
            # skip multiples of ten
            if num % 10 != 0:
                print(f"{num} is not a multiple of ten.")
            else:
                print(f"{num} is a multiple of ten.")

if __name__ == "__main__":
    skipper = NumberSkipper()
    skipper.main()