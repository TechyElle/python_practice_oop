class CheckNotEqual:
    def run(self):
        number_one = float(input("Enter first number: "))
        number_two = float(input("Enter second number: "))
        if number_one != number_two:
            print("Result is Not Equal")
        else:
            print("Result is Equal")
if __name__ == "__main__":
    CheckNotEqual().run()