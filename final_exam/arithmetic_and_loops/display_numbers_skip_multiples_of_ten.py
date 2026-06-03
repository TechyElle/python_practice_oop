class NumberSkipper:
    def __init__(self, start=0, end=100):
        self.start = start
        self.end = end

    def run(self):
        for num in range(self.start, self.end + 1):
            if num % 10 != 0:
                print(f"{num} is not a multiple of ten.")
            else:
                print(f"{num} is a multiple of ten.")

if __name__ == "__main__":
    NumberSkipper().run()
