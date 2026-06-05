class PrintOddRangeWhile:
    def run(self):
        counter = 0
        while counter <= 100:
            if counter % 2 != 0:
                print(f"Result is {counter}")
            counter += 1

if __name__ == "__main__":
    PrintOddRangeWhile().run()