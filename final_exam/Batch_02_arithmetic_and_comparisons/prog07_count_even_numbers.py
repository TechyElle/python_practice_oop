class CountEvenNumbers:
    def run(self):
        even_count = 0
        for iteration in range(10):
            if float(input(f"Enter number {iteration + 1}: ")) % 2 == 0:
                even_count += 1
        print(f"Result is {even_count}")

if __name__ == "__main__":
    CountEvenNumbers().run()