class DisplayDuplicates:
    def run(self):
        numbers = [input(f"Enter number {i + 1}: ") for i in range(10)]
        for value in set(numbers):
            if numbers.count(value) > 1:
                print(f"Result is {value}")
if __name__ == "__main__":
    DisplayDuplicates().run()