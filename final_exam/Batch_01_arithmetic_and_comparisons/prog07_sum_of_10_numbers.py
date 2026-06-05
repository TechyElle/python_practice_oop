class SumTenNumbers:
    def run(self):
        total_sum = 0
        for iteration in range(10):
            total_sum += float(input(f"Enter number {iteration + 1}: "))
        print(f"Result is {total_sum}")
if __name__ == "__main__":
    SumTenNumbers().run()