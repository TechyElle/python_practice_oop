class EvenCounter:
    def main(self):
        even_count = 0

        for i in range(10):
            num = int(input(f"Enter a number {i+1}: "))

            # check for even remainder
            if num % 2 == 0:
                even_count += 1

        print(f"Total even numbers: {even_count}")

if __name__ == "__main__":
    EvenCounter().main()