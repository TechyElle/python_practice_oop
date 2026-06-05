class Multiply:
    def run(self):
        number_one = float(input("Enter first number: "))
        number_two = float(input("Enter second number: "))
        print(f"Result is {number_one * number_two}")

if __name__ == "__main__":
    Multiply().run()