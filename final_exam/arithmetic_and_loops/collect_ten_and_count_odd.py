class OddCounter:
    def main(self):
        self.odd_count = 0

        for i in range(10):
            num = float(input(f"Enter a number {i+1}: "))

            # check for odd remainder
            if num % 2 != 0:
                self.odd_count += 1

        print(f"Total odd numbers: {self.odd_count}")

if __name__ == "__main__":
    OddCounter().main()