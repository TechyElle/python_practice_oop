class NumbersBetween:
    def run(self):
        start_number = int(input("Enter start number: "))
        end_number = int(input("Enter end number: "))
        for counter in range(min(start_number, end_number) + 1, max(start_number, end_number)):
            print(f"Result is {counter}")
if __name__ == "__main__":
    NumbersBetween().run()