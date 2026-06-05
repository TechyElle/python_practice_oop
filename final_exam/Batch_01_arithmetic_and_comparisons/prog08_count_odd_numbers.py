class CountOddNumbers:
    def run(self):
        odd_count = 0
        for iteration in range(10):
            if float(input(f"Enter number {iteration + 1}: ")) % 2 != 0:
                odd_count += 1
        print(f"Result is {odd_count}")

if __name__ == "__main__":
    CountOddNumbers().run() 